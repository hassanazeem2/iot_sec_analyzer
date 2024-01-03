from socket import timeout
from tabnanny import verbose
import scapy.all as scapy

def scan(target_ip):
    arp_request = scapy.ARP(pdst=target_ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False[0])

    devices_list = []
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(devices_info)

    return devices_list

# example of usage: 
# scan_result = scan("192.168.1.1/24")
# print(scan_result)
