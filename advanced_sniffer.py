from scapy.all import sniff, IP, TCP, UDP, Raw

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        
        print("\n[+] New Packet Captured")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

        # Protocol detection
        if packet.haslayer(TCP):
            print("Protocol: TCP")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
        else:
            print("Protocol: Other")

        # Payload extraction
        if packet.haslayer(Raw):
            print(f"Payload: {packet[Raw].load}")

sniff(prn=process_packet, store=False)