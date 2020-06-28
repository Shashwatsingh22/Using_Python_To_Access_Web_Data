#We are going to do make a connection to a PORT...,Send A GET request .... & then get some data..

import socket

sck=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=input("Enter the Host NAME:")
sck.connect((host,80))
cmd="GET https://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
sck.send(cmd)

while True:
    data=sck.recv(512)
    if(len(data)<1):
        break
    print(data.decode())

sck.close()