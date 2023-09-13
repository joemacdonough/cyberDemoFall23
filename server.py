import socket
from _thread import *
logins = 0
suffixes = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th']
password = 'hackermanorwoman'
server = socket.socket()
host = 'localhost'
port = 1400
address=('', port)
tCount = 0

def thread(connection):
    connection.send(str.encode('\rEnter password: '))
    clientNum = str(tCount)
    attempt = ''
    time = 0
    input = connection.recv(2048)
    while (not input.decode('utf-8').endswith('\n')) or time == 0:
        attempt += input.decode('utf-8')
        if attempt.endswith('\n'):
            break
        elif attempt.endswith('\x08'):
            attempt = attempt[0:len(attempt)-2]
        input = connection.recv(2048)
        time += 1
    print('Client '+clientNum+' password attempt: '+attempt)
    if attempt.strip() == password:
        print('Client '+clientNum+' login successful.')
        global logins
        logins += 1
        reply = (str.encode('\r\nCongratulations! You are the '+ str(logins) + suffixes[logins%10]+ ' successful code-cracker!\r\nPlease enter your name to be placed on our challenge wall: '))
        connection.send(reply)
        name = ''
        time = 0
        input = connection.recv(2048)
        while (not input.decode('utf-8').endswith('\n')) or time == 0:
            name += input.decode('utf-8')
            if name.endswith('\n'):
                break
            input = connection.recv(2048)
            time += 1
        reply2 = str.encode('\r\nThanks for participating, '+name.strip()+'!\r\n')
        connection.send(reply2)
    else:
        reply = str.encode("Incorrect password. Please reconnect and try again.")
        connection.send(reply)
        print(name.strip())

    connection.close()

try:
    server.bind(address)
except socket.error as e:
    print(str(e))

print('Accepting connections')
server.listen(10)

while True:
    Client, address = server.accept()
    #print('Connection established with '+address[0]+':'+str(address[1]))
    start_new_thread(thread, (Client,))
    tCount += 1
    print('Thread Count: ' + str(tCount))




