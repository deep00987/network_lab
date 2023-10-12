import socket
import json

HOST = socket.gethostname()
PORT = 8000
PACKET_SIZE = 1024


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    nums = [2, 1, 4, 12, 8]
    payload = json.dumps(nums).encode()
    client_socket.sendall(payload)
    
    res = client_socket.recv(PACKET_SIZE)
    print("Max num is: ", res.decode())
    
    client_socket.close()
    
     


if __name__ == "__main__":
    main()