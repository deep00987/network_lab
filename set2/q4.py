# 1. Capture 10000 packets (either online/offline)

# 2. Count the number of distinct host IP addresses and display them.

# 3. For each distinct pair of source/destination host IP addresses 
# determine the number of
# TCP/UDP segments exchanged and also the average payload length.
from scapy.all import *


def capture_packets(count=100):
    list_of_packets = sniff(count=count, offline='scapydmp.pcapng')
    return list_of_packets

def get_packet_details(pkts):
    host_dst_pairs = {}
    for pkt in pkts:
        # print(pkt.show())
        if not pkt.haslayer('IP'):
            continue
        
        #key-pair
        src, dest = pkt['IP'].src, pkt['IP'].dst
        sport, dport = None,None
        
        
        protocol = None
        payload_length = 0
        
        if pkt.haslayer('TCP'):
            protocol = 'TCP'
            sport = pkt[protocol].sport
            dport = pkt[protocol].dport
            payload_length = len(pkt['TCP'].payload)
            
        elif pkt.haslayer('UDP'):
            protocol = 'UDP'
            sport = pkt[protocol].sport
            dport = pkt[protocol].dport
            payload_length = len(pkt['UDP'].payload)

        else:
            # skip other packets that are not TCP or UDP
            continue
        
        key = (src, dest, sport, dport)
        
        if key not in host_dst_pairs:
            host_dst_pairs[key] = {
                "TCP": 0,
                "UDP": 0,
                "segments": 0,
                "total_length": 0  
            }
        
        host_dst_pairs[key][protocol] += 1
        host_dst_pairs[key]['segments'] += 1
        host_dst_pairs[key]['total_length'] += payload_length
        
    return host_dst_pairs

packets = capture_packets(100)
print(packets)

pkt_info_dict = get_packet_details(packets)
# print(pkt_info_dict)
print("\n\n========= Output =========\n\n")
print("+-----------------------+-----------------------+---------------+---------------+-----------------------+-----------------------+-----------------------+\t")
print("| Source IP\t\t|\tDestination IP\t|\tS-port\t|\tD-port\t|\tProtocol\t|\tNo of segments\t|\tAvg payload len |\t")
print("+-----------------------+-----------------------+---------------+---------------+-----------------------+-----------------------+-----------------------+\t")

for key in pkt_info_dict:
    print(f"|{str(key[0]).ljust(23)}|\t{key[1]}\t|\t{key[2]}\t|\t{key[3]}\t|\t{'TCP'if pkt_info_dict[key]['TCP'] > 0 else 'UDP' }\t\t|\t{pkt_info_dict[key]['segments']}\t\t|\t{pkt_info_dict[key]['total_length'] // pkt_info_dict[key]['segments']}\t\t|\t")

print("+-----------------------+-----------------------+---------------+---------------+-----------------------+-----------------------+-----------------------+\t")
