import socket
import threading
import json

HOST = socket.gethostname()
PORT = 8000
PACKET_SIZE = 1024

def handle_client(client_socket):
    req = client_socket.recv(PACKET_SIZE)
    data = json.loads(req.decode())
    
    res = max(data)
    
    payload = str(res).encode()
    
    client_socket.sendall(payload)
    

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("setting up server at {HOST}:{PORT}".format(HOST=HOST, PORT=PORT))
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"received connection from address: {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()
        # handle_client(client_socket)
    

if __name__ == '__main__':
    main()