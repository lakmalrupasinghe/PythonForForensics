
# PythonForForensics
This would contain different programming examples and use cases for Digital Forensics specially using python.

## These are the areas 
1. Data Extraction
2. File Carving
3. Log Anlaysis
4. Time line anlaysis



### Usage of Scapy library

'''
from scapy.all import *

def packet_callback(packet):
    if packet[TCP].payload:
        tcp_payload = str(packet[TCP].payload)
        if "HTTP" in tcp_payload:
            print("Found HTTP packet: ", tcp_payload)

# Start sniffing
sniff(filter="tcp", prn=packet_callback)

'''
