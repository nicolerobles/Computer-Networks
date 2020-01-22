#################################################################
# Name: Nicole Robles
# Date: January 17, 2020
# Description: UDP Ping Server
#################################################################

from socket import *
from random import randint
from time import sleep

# configurations
server_port = 12000
packet_size = 2048

# create server socket
server_socket = socket(AF_INET, SOCK_DGRAM)

# bind server socket to port number
server_socket.bind(('', server_port))

# loop to keep receiving messages
while (True):
    try:
        # receive the message from socket
        message, client_address = server_socket.recvfrom(packet_size)

        # simulated packet loss
        if(randint(0,9) < 4):
            # print("Simulated packet loss")
            sleep(1.1)
        else:
            # send message back to client
            server_socket.sendto(message, client_address)
    except:pass
