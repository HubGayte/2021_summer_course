import socket
ip='0.0.0.0'
p=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,p))

while 1:
    d,(ip,p)=s.recvfrom(1024)
    print('Sender: {} Port: {}.'.format(ip,p))
    print('Receive message: {}'.format(d))
    
