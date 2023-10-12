import socket
import json

HOST = socket.gethostname()
PORT = 8000
PACKET_SIZE = 1024


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    while True:
        num = input("Enter number")
        client_socket.send(num.encode())
        response = client_socket.recv(PACKET_SIZE).decode()
        result = False
        if response == 'True':
            result = True

        if result == False: print(f"The given number {num} is not prime")
        if result == True:
            print(f"The given number {num} is prime")
            break
        
    client_socket.close()
        
if __name__ == "__main__":
    main()