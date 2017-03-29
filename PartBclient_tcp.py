# CSC 138
# client-side echo tcp

from socket import *
import select
import sys
import time
serverName = 'localhost'
serverPort = 12000

def timeOutOrReceive():
   start = time.time()
   while (time.time() - start < 5):
      message = clientSocket.recv(1024)
      print 'received no message'
      if message:
         print 'From Server: '+ message
   return;

#socket.SOCK_STREAM for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

#connect has (( because it can take more than 1 parameter
try:
   clientSocket.connect((serverName, serverPort))
   print 'Connected to Server: ' + serverName
except:
   print 'unable to connect to server'
   sys.exit()

while 1:
   try:
      timeOutOrReceive()
      print 'timeout'
   except:
      continue
   else:
      message = (raw_input('Input lowercase sentence ("Quit" to end): '))
      clientSocket.send(message)
      modifiedMessage = clientSocket.recv(1024)
      message = modifiedMessage.upper()
      clientSocket.send(message)


      



print "  Connection end."
clientSocket.close()
