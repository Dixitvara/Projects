import socket

 

localIP     = "192.168.200.11"

localPort   = 20001

bufferSize  = 1024

 

msgFromServer       = "Dixit"

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
name = bytesAddressPair[0]
print("",name,"is connecting")
UDPServerSocket.sendto(bytesToSend, bytesAddressPair[1]) 

# Listen for incoming datagrams

while(True):

    # Sending a reply to client
    msg=input("Enter the Message : ")
    UDPServerSocket.sendto(str.encode(msg), bytesAddressPair[1])

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = format(bytesAddressPair[0])

    print("Message from ",name,":",(message))
