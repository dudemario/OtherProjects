#Codepad: http://codepad.org/znoMBskJ
# Message Sender
from socket import *
host = "10.96.192.108" # target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("Enter message to send or type 'exit': ")
    UDPSock.sendto(bytes(data, 'utf_8'), addr)
    if data == "exit":
        break
UDPSock.close()

#Codepad: http://codepad.org/E5zsh7a0
# Message Receiver
from socket import *
host = "10.96.192.108" # this computer
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ("Waiting to receive messages...")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print ("Received message: " + str(data)[2:-1])
    if data == "exit":
        break
UDPSock.close()
