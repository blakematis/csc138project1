#CSC 138
# server-side echo tcp

from socket import *
serverPort = 12000

#Sock_STREAM for tcp socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

#listen for tcp request
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
  connectionSocket, addr = serverSocket.accept()

  message = connectionSocket.recv(1024)
  while (message != "Exit"):
    capitalizedMessage = message.upper()
    connectionSocket.send(capitalizedMessage)
    message = connectionSocket.recv(1024)
  connectionSocket.close()
