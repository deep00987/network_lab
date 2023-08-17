import socket

def main():
    host = '127.0.0.1'
    port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        student_name = input("Enter student's name to get address info or 'exit' to quit: ")
        if student_name.lower() == 'exit':
            break

        client_socket.sendto(student_name.encode(), (host, port))
        data, _ = client_socket.recvfrom(1024)
        print("server >", data.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
