'''
Created on Mar 17, 2017
Server implementation of toUpper Case
@author: Blake
'''
from socket import*

serverPort = 12000

#create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

#bind socket to local port number 12000
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

#loop forever 
while 1:
    #Read from UDP socket into message, getting client's
    #address (client IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)
    
    #change string to uppercase
    modifiedmessage = message.upper();
    
    #send upper case string back to this client
    serverSocket.sendto(modifiedmessage, clientAddress)
    
    