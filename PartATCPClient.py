'''
Created on Mar 18, 2017
TCP Client for Echo client server and
convert to uppercase
@author: Blake
'''

from socket import*

serverName ='172.16.0.5'

serverPort = 12000




while 1:
    #create TCP socket for server, remote port 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    
    #connect to server
    clientSocket.connect((serverName,serverPort))
    
    #get user keyboard input
    message = ' '
    message = raw_input('input lowercase sentence:')
    
    
     #if message is quit close the connection on client-side
    if message == "quit":
        print("closed connection")
        break;
    
    #attach server name, port to message, then send into socket
    clientSocket.send(message)
    
    #read reply characters from socket into string
    modifiedMessage = clientSocket.recv(1024)
    
    #print out received string and close socket
    print 'From Server:', modifiedMessage
    clientSocket.close();
    
