#This is a very basic HTTP server which listens on port 8080,
#and serves the same response messages regardless of the browser's request. It runs on python v3
#Usage: execute this program, open your browser (preferably chrome) and type http://servername:8080
#e.g. if server.py and broswer are running on the same machine, then use http://localhost:8080

# Import the required libraries
from socket import *
import os.path

# Listening port for the server
serverPort = 8080

# Create the server socket object
serverSocket = socket(AF_INET,SOCK_STREAM)

# Bind the server socket to the port
serverSocket.bind(('',serverPort))

# Start listening for new connections
serverSocket.listen(1)

print('The server is ready to receive messages')


while 1:
    # Accept a connection from a client
    connectionSocket, addr = serverSocket.accept()

    # Retrieve the message sent by the client
    request = connectionSocket.recv(1024)

    fileObject = request.decode("utf-8").split(" ")[1][1:]
    #print(fileObject)

    #Checks whether file exsists
    if os.path.isfile(fileObject):
        response = b"HTTP/1,1 200 OK\n\n"
        #print("Image File exsists")
        with open(fileObject, 'rb') as f:
            response = response + f.read()
            connectionSocket.send(response)
    else:
        print("File does not exsist")
        response = "HTTP 404 not found\r\n"
        connectionSocket.send(response.encode())

    # Close the connection
    connectionSocket.close()

