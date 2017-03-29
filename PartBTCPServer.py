#Minh Phung, Blake Matis
#CSC 138
#Server-side echo TCP

from socket import *
import select # for select.select
import sys #for sys.exit()

serverPort = 12000
socketList = []  # empty array
clientConnection = 0
addrList = []

# Sock_STREAM for tcp socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

# listen for TCP request
# There can be up to 2 client connect to the same server
serverSocket.listen(2)

# socketList contain a  lists of availble sockets.
socketList.append(serverSocket)
print "The server is ready to receive."

while 1:
  ready_to_read, ready_to_write, in_error = select.select(socketList, [], [], 0)
  for socket1 in ready_to_read:           # socket1 is outer loop index 
    # establishing new connection
    if socket1 == serverSocket: # server has connection request(ready_to_read)
      socketConnection, addr = serverSocket.accept()
      socketList.append(socketConnection)
      addrList.append(addr)
      clientConnection = clientConnection + 1
      print "Client (%s, %s) is connected." %addr
    else: #if socket1 != serverSocket
      message = socket1.recv(1024)
      if clientConnection == 2:#indicated that a staple connection between the 2 client is established
        for socket2 in socketList:
          if (socket2 != serverSocket and socket2 != socket1):
              socket2.send(message)
              if message == "Quit":
                print "Client (%s, %s) is disconnected." %addrList[0]
                socketList.remove(socket1)
                print "Client (%s, %s) is disconnected." %addrList[1]
                socketList.remove(socket2)
                addrList = []
                clientConnection = clientConnection - 2
      elif (clientConnection == 1 and message == "Quit"):
        print "Client(%s, %s) is disconnected." %addr
        #socket1.close()
        socketList.remove(socket1)
        addrList = [] #empty list after removing
        clientConnection = clientConnection -1
      else:#there is no chatting if there is only one client connected to the server
        socket1.send("There is no client to chat with.\n")
