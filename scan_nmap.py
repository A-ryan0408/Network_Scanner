import nmap
import time

nm = nmap.PortScanner()

nm.scan(hosts='192.168.130.0/24', arguments='-sA')

for host in nm.all_hosts():
    if 'mac' in nm[host]['addresses']:
        print(f"Host: {host}, MAC Address: {nm[host]['addresses']['mac']}")
    else:
        print(f"Host: {host}, MAC Address: Not found")
    time.sleep(1)
    

