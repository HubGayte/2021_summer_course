from scapy.all import *

a=IP(src='10.9.0.3',dst='10.9.0.99')
b=ICMP(type=0)
p=a/b
send(p)
