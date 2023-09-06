import ipaddress
import scapy.all as sc

# Function to send an ICMP echo request and check for response
def send_icmp_echo_request(ip):
    packet = sc.IP(dst=str(ip)) / sc.ICMP() / "hello" # Create ICMP packet
# Send packet and receive response,verbose false means nothing will be shown in terminal
    response = sc.sr1(packet, timeout=2, verbose=False) 
    if sc.ICMP in response: # Check if response contains ICMP layer
        return True # Host is responsive
    return False # Host is not responsive

# Get the network address from user input
network = input("Enter the network address in CIDR notation (e.g., 34.110.128.0/24): ")

try:

    network = ipaddress.ip_network(network, strict=False)
except ValueError:
    print("Invalid network address format.")

responsive_hosts = [] # List to store responsive hosts
print(f"Scanning network {network}...")

try:
# Iterate through all hosts in the network and send ICMP echo requests
    for ip in network.hosts():
        if send_icmp_echo_request(ip):
            print(f"Host {ip} is responsive.")
            responsive_hosts.append(ip)
except Exception as e:
    pass #Ctrl+C pressed. Exiting gracefully.

#this block always executes
finally:
    print("stop sending packet")
    #printing the list of responsive host
    print("\nResponsive hosts:")
    for ip in responsive_hosts:
        print(ip)
