import socket

HOST = 'hsit.ac.in'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.send('GET http://127.0.0.1/hello.jpg HTTP/1.0\r\n\r\n'.encode())
picture = b''
while True:
    data = mysock.recv(5120)
    if (len(data) < 1):
        break
    
    picture = picture + data
mysock.close()

#print (picture)

pos = picture.find(b'\r\n\r\n')
print('Header length',pos)
print(picture[:pos].decode())

#print (pos)
picture = picture[pos+4:]

#print (picture)
content = mysock.read()
fhand = open("hello1.jpg", "wb")
fhand.write(content)
fhand.close()




