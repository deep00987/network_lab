import ipaddress
import concurrent.futures
from scapy.all import Ether, IP, TCP, ICMP, sr, sr1, srloop



def network_info(ip_cidr_addr):
    ip, cidr = ip_cidr_addr.split('/')
    cidr_num =  int(cidr)
    octates = ip.split('.')
    ip_bin_octates = [bin(int(ele)) for ele in octates]
    q = []
    
    for i in range(cidr_num):
        q.append('1')
        if (i + 1) % 8 == 0 and i != 32 - 1:
            q.append('.')
    for i in range(cidr_num, 32):
        q.append('0')
        if (i + 1) % 8 == 0 and i != 32 - 1:
            q.append('.')
    # print(q)
    netmask_bin_octates = [bin(int(ele, 2)) for ele in "".join(list(q)).split(".")]
    netmask = ".".join([str(int(ele, 2)) for ele in netmask_bin_octates])
    
    net_id_octates = []
    
    for e1, e2 in zip(ip_bin_octates, netmask_bin_octates):
        net_id_octates.append(int(e1, 2) & int(e2, 2))
    
    
    net_id = ".".join([str(ele) for ele in net_id_octates])
    
    res_obj = {
        "ip" : ip,
        "cidr": cidr_num,
        "netmask": netmask,
        "network_addr": net_id 
    }
    
    return res_obj

def get_all_network_hosts(ip_cidr):
    net_info = network_info(ip_cidr)
    cidr , network_addr = net_info['cidr'], net_info['network_addr']
    all_possible_ip = []
    all_possible_ip.append(network_addr)
    total_ip = 2 ** (32 - cidr) - 1
    
    net_id_octates = [int(ele) for ele in network_addr.split(".")]
    
    i = 0
    o1, o2, o3, o4 = net_id_octates

    while i < total_ip:
        if o4 + 1 > 255:
            o4 = 0
            if o3 + 1 > 255:
                o3 = 0
                if o2 + 1 > 255:
                    o2 = 0
                    if o1 + 1 > 255:
                        raise ValueError("Value out of range!")
                    else:
                        o1 += 1
                        all_possible_ip.append(f"{o1}.{o2}.{o3}.{o4}")
                else:
                    o2 += 1
                    all_possible_ip.append(f"{o1}.{o2}.{o3}.{o4}")
            else:
                o3 += 1
                all_possible_ip.append(f"{o1}.{o2}.{o3}.{o4}") 
        else:
            o4 += 1
            all_possible_ip.append(f"{o1}.{o2}.{o3}.{o4}")
        i += 1   
        

    # print(total_ip, network_addr)
    # print(all_possible_ip)
    if cidr <= 30:
        all_possible_ip.pop()
        all_possible_ip.pop(0)
    
    # all_possible_ip.pop()
    # all_possible_ip.pop(0)
    
    return all_possible_ip
    
def network_scan(hosts):
    alive = []
    for host in hosts:
        packet = IP(dst=host) / ICMP() / "Hello"

        # response = srloop(packet, count=1, verbose=False, timeout=1)[0]
        response = sr1(packet, verbose=False, timeout=1)
        
        if response:
            print(f"{host} --> responsive")
            alive.append(host) 
        
        # if len(response) == 0:
        #     continue
        
        # elif response[0][1][ICMP].type == 0:
        #     print(response[0][1][ICMP].type)
        #     print(f"{host} --> responsive")
        #     alive.append(host)
        # else:
        #     continue
        # if response == None:
        #     continue
        # elif response[0][1][ICMP].type == 0:
        #     print(f"{host} --> responsive")
        #     alive.append(host)
        
    print("All responsive host ip address -----")         
    print(alive)
            

ip = input("enter ip: ") 
hosts = get_all_network_hosts(ip)  

print("All host ip addresses in the network range -----")
print(hosts)

print("Scanning network to find responsive hosts -----")
network_scan(hosts)















# hosts1 = []
# network = ipaddress.IPv4Network(ip, strict=False)
# for host in network.hosts():
#     hosts1.append(str(host))
# print(network_info(ip))
# print(hosts, hosts1)
# print(hosts == hosts1)
#-----------------------------------------------------------------------------------------------
### testing ####
# test_cases = [
#     '192.168.1.1', 
#     '127.28.37.4', 
#     '10.11.127.1', 
#     '106.236.250.229',
#     '158.238.57.139',
#     '229.132.86.107',
#     '64.91.1.76'
# ]
# def get_all_hosts_module(ip):
#     hosts1 = []
#     network = ipaddress.IPv4Network(ip, strict=False)

#     for host in network.hosts():
#         hosts1.append(str(host))

#     return hosts1
    
# def test_methods(test_case):
#     for i in range(9, 33):
#         ipaddress = test_case + '/' + str(i)
#         print(ipaddress, get_all_hosts_module(ipaddress) == get_all_network_hosts(ipaddress))

# # Create a thread pool for concurrent execution
# with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
#     # Run the test function concurrently for each test case
#     executor.map(test_methods, test_cases)
