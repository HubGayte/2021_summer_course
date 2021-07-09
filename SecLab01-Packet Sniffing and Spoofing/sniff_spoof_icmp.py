#!/usr/bin/env python3
from scapy.all import*

def print_pkt(pkt):
    p=IP(src=pkt[IP].dst,dst=pkt[IP].src)/ICMP(type='echo-reply',code=0,id=pkt[ICMP].id,seq=pkt[ICMP].seq)/pkt[Raw].load
    send(p)

pkt = sniff(iface="br-d3a9c727d803", filter='icmp[icmptype]==icmp-echo', prn=print_pkt)

