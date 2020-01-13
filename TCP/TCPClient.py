#################################################################
# Name: Nicole Robles
# Date: January 10, 2020
# Description: TCP Client
#################################################################

# Sample command to run the client code: python TCPClient.py server_ip server_port filename

from socket import *

# create clinet socket
client_socket = socket(AF_INET, SOCK_STREAM)

# set server IP address
server_ip = input("Please, enter server IP adrress: ")
# set server port number
server_port = input("Please, enter server port number: ")

# connect to server socket
client_socket.connect((server_ip, int(server_port)))
print("\nConnection established.\n")

# generate message to send
message = input("Please, enter message to send: ")
request = 'GET /' + message + ' HTTP/1.1'
client_socket.sendto(request, (server_ip, int(server_port)))
print "HTTP request to server: \n" + request + "\n" + "Host: " + server_ip +"\n"

# receive message from server
received_message = client_socket.recv(2048)
print "HTTP response from server: \n" + received_message

# close client socket
client_socket.close()
