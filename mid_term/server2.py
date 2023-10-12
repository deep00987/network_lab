import socket
import threading

HOST = socket.gethostname().split(".")[0]
PORT = 8000
PACKET = 1024

def is_prime(num):
    if num < 2:
        return False
    
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True


def handle_client(client_socket):
    while True:
        req = client_socket.recv(PACKET)
        data = int(req.decode())
        result = is_prime(data)
        print(result, str(result).encode())
        client_socket.sendall(str(result).encode())
        
        if result == True:
            break
        
        

    
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("setting up server at {HOST}:{PORT}".format(HOST=HOST, PORT=PORT))
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"received connection from address: {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()
        
        

if __name__ == "__main__":
    main()