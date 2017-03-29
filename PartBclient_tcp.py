# CSC 138
# client-side echo tcp

from socket import *
serverName = 'localhost'
serverPort = 12000

# socket.SOCK_STREAM for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect has (( because it can take more than 1 parameter
clientSocket.connect((serverName, serverPort))

message = raw_input('Input lowercase sentence("Quit" to end): ')

while 1:

   try:
      message.recv(1024)
      if message:
         print 'From Server: '+ message
   except:
      pass
   clientSocket.send(message)
   modifiedMessage = clientSocket.recv(1024)
   message = modifiedMessage.upper()
   clientSocket.send(message)


clientSocket.send(message)
print "  Connection end."
clientSocket.close()
