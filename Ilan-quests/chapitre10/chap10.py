from scapy.all import sniff, IP, TCP, UDP, ICMP

def afficher_paquet(pkt):
    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        proto = "?"
        info = ""
        
        if TCP in pkt:
            proto = "TCP"
            info = f"{pkt[TCP].sport} → {pkt[TCP].dport}"
        elif UDP in pkt:
            proto = "UDP"
            info = f"{pkt[UDP].sport} → {pkt[UDP].dport}"
        elif ICMP in pkt:
            proto = "ICMP"
            info = f"Type {pkt[ICMP].type}"
        
        print(f"{src:15} → {dst:15} {proto:6} {info}")

print("Sniffer lancé (Ctrl+C pour arrêter)")
sniff(prn=afficher_paquet, store=0)