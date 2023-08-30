# 1. Capture 10000 packets (either online/offline)

# 2. Count the number of distinct host IP addresses and display them.

# 3. For each distinct pair of source/destination host IP addresses determine the number of
# TCP/UDP segments exchanged and also the average payload length.

from scapy.all import *


def capture_packets(count=100):
    list_of_packets = sniff(count=count, offline='scapydmp.pcapng')
    return list_of_packets

def getHostIps(pkts):
    hosts = set()
    for pkt in pkts:
        # print(pkt)
        if pkt.haslayer('ARP'):
            # print("source: ", pkt['ARP'].psrc)
            continue
        else:
            # print("source: ", pkt['IP'].src)
            if pkt['IP'].src not in hosts:
                hosts.add(pkt['IP'].src)
    
    return hosts

packets = capture_packets(10000)
print(packets)

all_hosts = getHostIps(packets)
print("\n\n========= unique host IPs =========\n\n")
for (idx, host) in enumerate(all_hosts):
    print(idx + 1, " > ", host)