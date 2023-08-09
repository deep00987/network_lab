import socket

def main():
    host = "127.0.0.1"
    port = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        message = input("client > ")
        client.send(message.encode("utf-8"))
        if message.lower() == "quit":
            break
        response = client.recv(1024).decode("utf-8")
        if not response: 
            continue
        print(f"Server > {response}")
        

    client.close()

if __name__ == "__main__":
    main()
