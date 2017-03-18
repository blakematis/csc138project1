'''
Created on Mar 18, 2017
TCP Server for client/server echo to upper case
@author: Blake
'''
from socket import*

serverPort = 12000

#create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('',serverPort))

#server begins listening for incoming TCP bSupportsAsyncRequests
serverSocket.listen(1)
print 'The server is ready to receive'

#loop forever
while 1:
    #server waits on accept() for incoming requests,
    #new socket created on return 
    connectionSocket, addr = serverSocket.accept()
    
    #read bytes from socket(but not address as in UDP)
    message = connectionSocket.recv(1024)
    
    #set message to uppercase
    modifiedMessage = message.upper()
    
    #send message to client via port
    connectionSocket.send(modifiedMessage)
    
    connectionSocket.close()