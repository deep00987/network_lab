from datetime import datetime
import socket
import signal
import sys
import json
import threading

class SokServer(object):
    """
    Socket server class
    
    request struct --> {
        method : GET | POST | PUT | DELETE 
        payload ?: {data} OR None (optional)
        msg: "message"
    }
    
    response struct --> {
        status: NUMBER
        data: response data OR error msg
    }
    
    """
    def __init__(self, port=9999):
        self.host = socket.gethostname().split('.')[0]
        self.port = port
        print("host: ", self.host, "post: ", self.port)
        
    def start_server(self):
        """
        Start socket server
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        try:
            print("setting up server at {host}:{port}".format(host=self.host, port=self.port))
            self.socket.bind((self.host, self.port))
            print("server started at port: {port}".format(port=self.port))
            
        except Exception as e:
            print("Error setting up server")
            self.stop_server()
            sys.exit(1)
        
        # start listenting for incoming connection
        self.listen() 

    def listen(self):
        """
        listen for incoming connection/request to the server 
        """
        self.socket.listen(5)
        while True:
            
            clientSok, addr = self.socket.accept()
            clientSok.settimeout(30)
            print(f"Received connection from address: {addr}")
            ## TODO: handle conncurrent connection(Threads)
            
            threading.Thread(target=self.handle_request, args=(clientSok, addr)).start()
            # self.handle_request(clientSok, addr)

    def handle_request(self, client, address):
        """
            handle incoming request and send appropriate response
        """
        PACKET = 1024
            
        try:
            req = client.recv(PACKET)
            decoded_data = json.loads(req.decode())
            print("received data: ", decoded_data)
            
            # Reject any request other than req with GET method
            
            if decoded_data["method"] != "GET":
                raise Exception("Unknown request method or method not supported")
            
            response = {
                "status" : 200,
                "data": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            }
            
            json_response = json.dumps(response)
            client.sendall(json_response.encode())

        except Exception as e:
            print(e)
            err_res = {
                "status" : 500,
                "data": str(e)
            }  
            client.sendall(json.dumps(err_res).encode())

    def stop_server(self):
        """
        Shutdown server
        """
        try:
            print("Shutting down server ... ")
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
            sys.exit(1)
        except Exception as e:
            pass
        

def shutdownServer(sig, unused):
    """
    Shutsdown server from a SIGINT recieved signal
    """
    server.stop_server()
    sys.exit(1)

signal.signal(signal.SIGINT, shutdownServer)
server = SokServer(6969)
server.start_server()
