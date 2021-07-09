import socket

ip='10.9.0.5'
p=9999
d=b'uuuudp_is_coming'

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(d,(ip,p))

