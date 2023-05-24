import socket
msgFromClient       = "Dixit"

bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.200.20", 20001)

bufferSize          = 1024
# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
name=(msgFromServer[0])
print("",name,"is connecting")
while True:
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            msg1 = format(msgFromServer[0])
            print("From ",name,":",msg1)

            msg2=input("Enter the message : ")
            UDPClientSocket.sendto(str.encode(msg2), serverAddressPort)
            
