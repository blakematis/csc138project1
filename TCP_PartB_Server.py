'''
Created on Mar 27, 2017

@author: Blake
'''
from socket import *
import select
import sys

#server ip address
HOST = ''

#server Port
SERVER_PORT = 12000

#lists of connected sockets
socketList = []

#listed of connected addressess
addrList = []

#this is unused for now I have not implemented it like your program has Minh
clientConnection = 0
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST,SERVER_PORT))

#listen for only 2 clients
serverSocket.listen(2)

#add the serverSocket to the socketList
socketList.append(serverSocket)

#explains that server is online and what port it is accessible from
print 'The Server is ready to receive on port: ' + str(SERVER_PORT)

def forwardMessage (serverSocket, sock, message):
        #only want to send to the other client
        for socket in socketList:
            if socket != serverSocket and socket != sock:
                try:
                    socket.send(message)
                except:
                    continue
                
while 1:
    ready_to_read, ready_to_write, in_error = select.select(socketList, [], [], 0)
    for sock in ready_to_read:
        if sock == serverSocket:
            socketConnection, addr = serverSocket.accept()
            socketList.append(socketConnection)
            clientConnection = clientConnection + 1;
            connectionMessage = "Client: "+ str(clientConnection) +" (%s, %s) is connected" %addr
            sock.send(connectionMessage)
        try:
            # attempt to recieve message from client
            message = sock.recv(1024)
            if message: 
                forwardMessage(serverSocket, sock, message)
        except:
            continue