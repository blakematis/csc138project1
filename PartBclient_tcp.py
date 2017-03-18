# CSC 138
# client-side echo tcp

from socket import *
import select #for select.select
import sys #for sys.stdin
serverName = 'localhost'
serverPort = 12000

# socket.SOCK_STREAM for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect has (( because it can take more than 1 parameter
clientSocket.connect((serverName, serverPort))

sys.stdout.write('--> ')  # add "To: " to stdin
sys.stdout.flush() #flush request for enter

while 1:
  socketList = [sys.stdin, clientSocket]
  ready_to_read, ready_to_write, in_error = select.select(socketList, [], [], 0)
  for socket1 in ready_to_read:
    if socket1 == clientSocket:
      reply = clientSocket.recv(1024)
      if reply == "Exit\n":
        print "Connection end."
        sys.exit()
        clientSocket.close()
      sys.stdout.write(reply)
      sys.stdout.write('--> ')
      sys.stdout.flush()  
    else:
      message = sys.stdin.readline() # read stdin as the msg
      clientSocket.send(message)
      sys.stdout.write('--> ')
      sys.stdout.flush() # flush the "To: "
      if message == "Exit\n": #stdin.readline() also p8ick up enter
        print "Connection end."
        sys.exit()     # for ready_toread etc...
        clientSocket.close()
