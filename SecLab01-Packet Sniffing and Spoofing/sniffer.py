#!/usr/bin/env python3
from scapy.all import*

def print_pkt(pkt):
    pkt.show()

#pkt = sniff(iface="ens33", filter="icmp" , prn=print_pkt)
pkt = sniff(iface="br-d3a9c727d803", filter='icmp', prn=print_pkt)

