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

    '''
    Extract filename from the GET request
    Open file if it exists
    Read content of the file into string
    Append the string to the HTTP 200 OK response
    Otherwise HTTP 404 not found
    
    String value of request when content is appended to response
    b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\n\r\n'
    b'GET /html.jpg HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nReferer: http://localhost:8080/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\n\r\n'
    b'GET /servers.jpg HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nReferer: http://localhost:8080/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\n\r\n'
    b'GET /favicon.ico HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nReferer: http://localhost:8080/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\n\r\n'

    
    '''
    
    fileObject = request.decode("utf-8").split(" ")[1][1:]
    #print(fileObject)
    
    #Checks whether file exsists
    if os.path.isfile(fileObject):
        print("File exsists")
        with open(fileObject) as f:
            response = f.read()
    else:
        print("File does not exsist")
        response = "HTTP 404 not found\n\n"

    print(response)
    
    #send HTTP response back to the client
    connectionSocket.send(response.encode())

    # Close the connection
    connectionSocket.close()

