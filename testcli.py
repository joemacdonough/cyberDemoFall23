import socket 
client = socket.socket()

host = 'localhost'
port = 1400
address = (host,port)
print('connecting')
try:
    client.connect(address)
except socket.error as e:
    print(str(e))

while True:
    resp = client.recv(2048)
    print(resp.decode('utf-8'))
    message = input()
    client.send(str.encode(message))