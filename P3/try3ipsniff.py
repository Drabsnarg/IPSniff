from scapy.all import sniff

# Global variable to control the packet capture loop
stop_capture = False

def packet_callback(packet):
    print(packet.summary())

    # Check if the stop_capture flag is set
    if stop_capture:
        # Stop capturing packets
        raise KeyboardInterrupt

try:
    sniff(prn=packet_callback, filter="")
except KeyboardInterrupt:
    print("Packet capture stopped.")
