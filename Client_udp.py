# CSC 138
# client-side echo udp

from socket import *
serverName = 'localhost'
serverPort = 12000
# socket.SOCK_DGRAM for UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input("Input lowercase sentence('Exit' to end): ")
while (message != "Exit"):
  clientSocket.sendto(message, (serverName, serverPort))
  modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
  print 'From Server: ', modifiedMessage
  message = raw_input('Input lowercase sentence("Exit" to end: ')

print 'Connection closed.'

clientSocket.close()
