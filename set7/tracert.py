from scapy.all import *


def traceroute(dst_ip, max_hops):
    print(f"Tracing route to {dst_ip} using ICMP")

    for i in range(1, max_hops + 1):
        packet = IP(dst=dst_ip, ttl=i) / ICMP()
        reply = sr1(packet, timeout=2, verbose=False, iface='Ethernet')
        if reply is None:
            print(f"At hop {i}   : * * * *")
        elif reply[ICMP].type == 0: #Echo reply
            print(f"At hop {i}   : {reply[IP].src} (Destinition reached)")
            break
        elif reply[ICMP].type == 11: #Time Limit Exceeded
            print(f"At hop {i}   : {reply[IP].src} (Intermediate router)")

def traceroute2(dst_ip, max_hops):
    print(f"Tracing route to {dst_ip} using UDP")
    
    for i in range(1, max_hops + 1):
        pkt = IP(dst=dst_ip, ttl=i) / UDP(dport=33434)
        reply = sr1(pkt, timeout=3, verbose=0)
        if reply is None:
            print(f"At hop {i}   : * * * *")
        elif reply.type == 3:
            print(f"At hop {i}   : {reply.src} (Destinition reached)")
            break
        else:
            print(f"At hop {i}   : {reply.src} (Intermediate router)")


traceroute2('142.250.182.46', 24)
print("\n---------------------------------------------------------\n")
traceroute('142.250.182.46', 24)