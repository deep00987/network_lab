import socket
import threading
import csv

def load_student_data(file_path):
    student_data = {}
    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            name, address = row
            student_data[name] = address
    return student_data

def find_student_info(file_path, student_name):
    res = "student not found"
    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            name, address = row
            if name == student_name:
                res = f"Name: {name}, Address: {address}"
                break
            # student_data[name] = address
    return res

def handle_UDP_requests(client_address, server_socket, data, file_path):
    student_name = data.decode()
    student_data = find_student_info(file_path, student_name)
    print("client >", student_name)
    reply = student_data.encode()
    server_socket.sendto(reply, client_address)


def main():
    host = '127.0.0.1'
    port = 9999
    file_path = './data.csv'

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print("UDP server listening on", host, "port", port)

    while True:
        data, address = server_socket.recvfrom(1024)
        client_handler = threading.Thread(target=handle_UDP_requests, args=(address, server_socket, data, file_path))
        client_handler.start()
        
if __name__ == "__main__":
    main()

