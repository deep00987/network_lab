from scapy.all import sniff, ICMP, IP, sr1

def send_echo():
    ip = input("Enter input ip address: ")
    icmp_packet = IP(dst=ip)/ICMP(type=8, code=0)/ "Hello"
    response = sr1(icmp_packet, verbose=True, timeout=1)

    if response:
        print(f"Host {ip} is responsive")
    else:
        print(f"Host {ip} is not responsive")
        


def main():
    # dmp = sniff(count=1000)
    # print(dmp.summary())
    send_echo()

if __name__ == "__main__":
    main()
    
    