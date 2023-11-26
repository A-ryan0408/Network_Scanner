import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=10, verbose=False)[0]

    mac_addresses = []
    for element in answered_list:
        mac_addresses.append({"ip": element[1].psrc, "mac": element[1].hwsrc})
    return mac_addresses

def display_result(results):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results:
        print(client["ip"] + "\t\t" + client["mac"])

target_ip = "192.168.1.0/24"  # Adjust the IP range as needed
scan_result = scan(target_ip)
display_result(scan_result)
