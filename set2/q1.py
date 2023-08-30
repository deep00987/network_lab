# 1. Capture 10000 packets (either online/offline)

# 2. Count the number of distinct host IP addresses and display them.

# 3. For each distinct pair of source/destination host IP addresses determine the number of
# TCP/UDP segments exchanged and also the average payload length.
from scapy.all import *


def capture_packets(count=100):
    list_of_packets = sniff(count=count, offline='scapydmp.pcapng')
    return list_of_packets

packets = capture_packets(10000)
print(packets.summary()) # question 1 capture 10k packets on/off
