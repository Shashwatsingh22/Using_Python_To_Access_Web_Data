#Creating Socket It Does't mean that we are sending any data....we are just making an call...
import socket
sck=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=input("Enter The HostName:")
sck.connect((host,80))