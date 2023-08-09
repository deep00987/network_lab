import socket
import threading

clients = []

def handle_client(client_socket):
    clients.append(client_socket)
    
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"client > {message}")
            
            response = input("server > ")
            for client in clients:
                client.send(response.encode("utf-8"))
        except Exception as e:
            print(f"Error: {e}")
            break

    clients.remove(client_socket)
    client_socket.close()

def send_messages():
    while True:
        response = input("server > ")
        for client in clients:
            client.send(response.encode("utf-8"))

def main():
    host = "127.0.0.1"
    port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    send_thread = threading.Thread(target=send_messages)
    send_thread.start()

    while True:
        client_socket, client_address = server.accept()
        print(f"\nAccepted connection from {client_address[0]}:{client_address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()




