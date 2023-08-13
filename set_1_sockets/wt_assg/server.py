import socket
import threading

def handle_client(client_socket):
    
    receive_handler = threading.Thread(target=receive_messages, args=(client_socket,))
    send_handler = threading.Thread(target=send_messages, args=(client_socket,))

    receive_handler.start()
    send_handler.start()

    receive_handler.join()
    send_handler.join()

    client_socket.close()

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"{data}")
        except Exception as e:
            print(str(e))
            break

def send_messages(client_socket):
    while True:
        message = "server > "
        message += input()
        try:
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            # client_socket.close()
            print(str(e))
        

def main():
    server_ip = '127.0.0.1'
    server_port = 9999

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"TCP server listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Recieved connection from {client_address[0]}:{client_address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
