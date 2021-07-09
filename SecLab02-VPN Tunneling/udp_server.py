from scapy.all import*

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface="eth0", filter="icmp or arp" , prn=print_pkt)
