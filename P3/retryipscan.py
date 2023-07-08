from scapy.all import *
import tkinter as tk
from tkinter import filedialog
import threading
import csv
import keyboard

def packet_handler(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} -- Destination IP: {dst_ip}")

        # Save the packet information to the CSV file
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([src_ip, dst_ip])

def terminate_program():
    global terminate_flag
    terminate_flag = True

def select_file():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

# Create the main GUI window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask the user to select the file path using a dialog box
file_path = ""
root.after(0, select_file)
root.mainloop()

# Set the network interface to monitor (replace with the appropriate interface name)
interface = "Ethernet"

# Start sniffing packets on the specified interface
sniff_thread = AsyncSniffer(iface=interface, prn=packet_handler)
sniff_thread.start()

# Create a thread to check for termination by pressing the "Q" key
keyboard_thread = threading.Thread(target=lambda: keyboard.wait("q"), daemon=True)
keyboard_thread.start()

# Wait for the termination condition
keyboard_thread.join()

# Terminate the program
terminate_program()

# Wait for the sniffing thread to finish
sniff_thread.join()
