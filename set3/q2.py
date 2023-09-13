from scapy.all import IP, TCP, sr1
import threading

def port_scan(host, start_port, end_port, open_ports):
    for port in range(start_port, end_port):
        # TCP SYN packet
        # print("scanning ", port)
        tcp_packet = IP(dst=host) / TCP(dport=port, flags="S")
        
        response = sr1(tcp_packet, timeout=1, verbose=False)
        
        if response is not None and response['TCP'].flags == "SA":
            print("open --> ", port)
            open_ports.add(port)

def concurrent_port_scan(ip_addr, num_threads=16, ports_per_thread=64):
    open_ports = set()
    threads = []

    for i in range(num_threads):
       
        start_port = i * ports_per_thread
        end_port = start_port + ports_per_thread

        thread = threading.Thread(target=port_scan, args=(ip_addr, start_port, end_port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports

if __name__ == "__main__":
    ip_addr = input("Enter the Network Address : ")
    print("scanning top ports -->")
    open_ports = concurrent_port_scan(ip_addr)

    print("all open Ports : ")
    print(open_ports)
