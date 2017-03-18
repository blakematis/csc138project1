'''
Created on Mar 17, 2017
Client implementation of UDP echo
@author: Christopher Blake Matis
'''

#include Python's socket library
from socket import*

#set variables serverName and serverPort
serverName = '172.16.0.5'
serverPort = 12000


while 1:
    
    #create UDP socket for server
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #get user keyboard input
    message = ' '
    message = raw_input('input lowercase sentence:')
    
    #if message is quit close the connection on client-side
    if message == "quit":
        print("closed connection")
        break
    
    #check if message equals 'quit' and then close the connection   
    #attach server name, port to message, then send into socket
    clientSocket.sendto(message,(serverName,serverPort))
    
    #read reply characters from socket into string
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    
    #print out received string and close socket
    print modifiedMessage
    clientSocket.close();
    
