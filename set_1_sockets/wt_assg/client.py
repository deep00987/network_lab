import socket
import threading

def send_messages(client_socket):
    while True:
        message = "client > "
        message += input()
        try:
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(str(e))
            # client_socket.close()
            break

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"{data}")
        except Exception as e:
            # client_socket.close()
            print(str(e))
            break

def main():
    
    server_ip = '127.0.0.1'
    server_port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    receive_handler = threading.Thread(target=receive_messages, args=(client_socket,))
    send_handler = threading.Thread(target=send_messages, args=(client_socket,))

    send_handler.start()
    receive_handler.start()

    send_handler.join()
    receive_handler.join()
    
    client_socket.close()

if __name__ == "__main__":
    main()
