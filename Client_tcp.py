# CSC 138
# client-side echo tcp

from socket import *
serverName = 'localhost'
serverPort = 12000

# socket.SOCK_STREAM for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect has (( because it can take more than 1 parameter
clientSocket.connect((serverName, serverPort))

message = raw_input('Input lowercase sentence("Exit" to end): ')

while (message != "Exit"):
  clientSocket.send(message)
  modifiedMessage = clientSocket.recv(1024)
  print 'From Server: ', modifiedMessage
  message = raw_input('Input lowercase sentence("Exit" to end): ')

clientSocket.send(message)
print "  Connection end."
clientSocket.close()
