from scapy.all import sr1, IP, ICMP

# Ping
packet = sr1(IP(dst="8.8.8.8")/ICMP())

# Show packet info
if packet:
	packet.show()