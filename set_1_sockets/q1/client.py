import socket

HOST = "127.0.0.1"
PORT = 32768
BUFF_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    skt.connect((HOST, PORT))
    print(f"Client connected on {HOST}:{PORT}")

    print("Client --> hello server what's the current date ?")
    msg = "hello server what's the current date ?".encode()

    skt.sendall(msg)

    res = skt.recv(BUFF_SIZE).decode()

    print("Server --> ", res)

    print("Client --> Got the time, Thank you")
    skt.sendall("Got the time, Thank you".encode())

    skt.close()

