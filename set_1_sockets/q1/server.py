from datetime import datetime
import socket

# import signal
# import sys

HOST = "127.0.0.1"
PORT = 32768
BUFF_SIZE = 1024

# def signal_handler(sig, frame, conn):
#     print("server shutting down")
#     conn.shutdown(socket.SHUT_RDWR)
#     conn.close()
#     sys.exit(0)

# signal_handler(signal.SIGINT, None, conn)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Server listining on {HOST}:{PORT}")
    
    conn = None
    try:
        conn, addr = server.accept()
            
        msg = f"current date-time : {datetime.now()}".encode()
        data = conn.recv(BUFF_SIZE)
        print ("Client --> ", data.decode())
        
        print(f"Server --> current date-time : {datetime.now()}")
        conn.send(msg)
        
        data = conn.recv(BUFF_SIZE)
        print(f"Client --> ", data.decode())

        conn.close()

        print("connection closed.")

    except KeyboardInterrupt:
        print("key pressed ctrl + c")
        server.shutdown(socket.SHUT_RDWR)
        server.close()

    server.close()

if __name__ == "__main__":
    main()
        
