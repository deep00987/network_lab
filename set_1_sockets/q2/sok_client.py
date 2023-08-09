import socket
import json

HOST = socket.gethostname().split('.')[0]
PORT = 6969
BUFF_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    skt.connect((HOST, PORT))
    req = {}
    req["method"] = "GET"
    
    print(f"Client connected on {HOST}:{PORT}")
    data = input("Enter expression to evaluate: ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    msg = "What's the current date ?"
    req["msg"] = msg
    skt.sendall(json.dumps(req).encode())    

    print("Client request: ", req)

    data = skt.recv(BUFF_SIZE)
    res = json.loads(data.decode())
    
    print("response from server: ", res)
    
    print(f"Server --> status: {res['status']}, data: {res['data']}")
    
    skt.close()
