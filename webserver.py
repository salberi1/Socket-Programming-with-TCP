#import socket module
# Finish connecting with SSH with github
from socket import *
import sys # In order to terminate the program

serverPort = 6767

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('172.20.165.59', serverPort))
serverSocket.listen(1)
	

# Server should be up and running and listening to the incoming connections
while True:
    print("Ready to serve ...")
    
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode('utf-8')
        #print(message)

        # Extract the path (which is the second part of HTTP header)
        # of the requested object from the message.
        # assuming message holds the data from the previous line(s) of code
        filename = message.split ()[1]
        # Because the extracted path of the HTTP request includes
        # a chara"HTTP /1.1 404 Not Found\r\n\r\n"cter ‘\’, we read the path from the second character
        f = open(filename [1:])
        # Store the entire content of the requested file in a temporary buffer
        outputdata = f.read()
        
        connectionSocket.send("HTTP /1.1 200 OK\r\n\r\n". encode ())
        
        #Send the content of the requested file to the client
        #Assuming connectionSocket has been created above
        for i in range(0, len(outputdata )):
            connectionSocket.send(outputdata[i]. encode ())
        connectionSocket.send ("\r\n". encode ())
        connectionSocket.close()

    except IOError:
        connectionSocket.send("HTTP /1.1 404 Not Found\r\n\r\n". encode ())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()
    

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
