import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            response = client_socket.recv(1024).decode("utf-8")
            print(f"server > {response}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_messages(client_socket):
    while True:
        message = input("client > ")
        client_socket.send(message.encode("utf-8"))
        if message.lower() == "quit":
            break

def main():
    host = "127.0.0.1"
    port = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

if __name__ == "__main__":
    main()


