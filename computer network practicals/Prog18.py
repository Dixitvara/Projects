import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 80))

cmd = 'GET http://127.0.0.1/hello.txt HTTP/1.0\r\n\r\n'.encode()
new_data = b''
mysock.send(cmd)
while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    new_data = new_data + data

pos = new_data.find(b'\r\n\r\n')
print(new_data[pos+4:].decode())
mysock.close()
