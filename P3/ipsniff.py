from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} -- Destination IP: {dst_ip}")

# Set the network interface to monitor (e.g., "eth0" for Ethernet, "wlan0" for Wi-Fi)
interface = "Ethernet"

# Start sniffing packets on the specified interface
sniff(iface=interface, prn=packet_handler)
