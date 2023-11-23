from scapy.all import *

def get_mac(ip_address):
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=1, timeout=2, verbose=False)
    for s,r in resp:
        return r[ARP].hwsrc
    return None

def prn(pkt):
    
    if pkt[ARP].op == 2:  # is-at (response)
        act_mac = get_mac(pkt[ARP].psrc)
        res_mac = pkt[ARP].hwsrc
        
        if act_mac != res_mac:
            return f"[!] Possible Arp poisoning --> Response: {pkt[ARP].hwsrc} has address {pkt[ARP].psrc}"

        return f"[*] Response: {pkt[ARP].hwsrc} has address {pkt[ARP].psrc}"


sniff(filter='arp', count=150, prn=prn)

