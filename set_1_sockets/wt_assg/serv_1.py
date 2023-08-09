import socket
import threading

def handle_req(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                continue
            print(f"client > {message}")
            
            # if message == "quit":
            #     break
            
            response = input("server > ")
            client_socket.send(response.encode("utf-8"))
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        print(f"Connection received from {client_address[0]}:{client_address[1]}")
        client_handler = threading.Thread(target=handle_req, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
