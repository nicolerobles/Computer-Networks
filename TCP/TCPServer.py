#################################################################
# Name: Nicole Robles
# Date: January 10, 2020
# Description: TCP Server
#################################################################

from socket import *

# create server socket
server_socket = socket(AF_INET, SOCK_STREAM)
# bind socket to port number
server_socket.bind(('', 12001))
# keep socket listening to connections
server_socket.listen(1)
print("Server is ready to connect...\n")

# find the host name
host_name = gethostname()
# find the host IP by looking up the host name
host_IP = gethostbyname(host_name)

# run forever loop to connect and receive messages
while(True):
    # create connection socket
    connection_socket, address = server_socket.accept()
    print("Connection established.\n")

    # receive message from connection socket
    incoming_message = connection_socket.recv(2048)

    # print HTTP request from the client
    print "HTTP request: \n" + incoming_message + "\n" + "Host: " + host_IP +"\n"

    # modify message
    modified_message = incoming_message.split(" ")
    name_of_file = modified_message[1]
    name_of_file = name_of_file.replace("/", "")
    #incoming_message.upper()
    #print("Modified message: {}".format(modified_message.decode()))

    # print name of the file being fetched
    print "Object to be fetched: " + name_of_file

    try:
        # when file exists
    	if open(name_of_file):
    		# print the content of the file
    		file_content = open(name_of_file, "r").read()
    		print "Object content: \n" + file_content
            # send back HTTP response to client
    		HTTP_response = "HTTP/1.1 200 OK \n\n" + str(file_content)
    		server_socket.sendto(HTTP_response, address)

    # when file does not exist
    except:
    	# send back HTTP response to client
    	HTTP_response = "HTTP/1.1 404 Not Found"
    	server_socket.sendto(HTTP_response, address)

    print "HTTP response message: \n" + HTTP_response

    # # receive message from connection socket
    # incoming_message = connection_socket.recv(2048)
    # #print("Received message: {}".format(incoming_message.decode()))
    #
    # # modify message
    # modified_message =
    # #incoming_message.upper()
    # print("Modified message: {}".format(modified_message.decode()))

    # send message back to client
    # connection_socket.send(modified_message)
    # print("Message sent.\n")

    # close connection socket
    connection_socket.close()
