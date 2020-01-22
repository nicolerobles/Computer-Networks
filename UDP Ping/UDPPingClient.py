#################################################################
# Name: Nicole Robles
# Date: January 17, 2020
# Description: UDP Ping Client
#################################################################

from socket import *
from time import time, sleep, clock
from sys import argv
import datetime

# command line input check
if(len(argv) < 4):
    print("Usage: python {} [ip] [port] [packets]".format(argv[0]))
    exit()

# configurations
setdefaulttimeout(1)
packet_size = 2048

# parse command line inputs
server_ip = argv[1]
server_port = argv[2]
ping_count = int(argv[3])

# create the timestamps
def create_timestamp():
    info = datetime.datetime.timetuple(datetime.datetime.today())[:]
    weekdays = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
    months = ("Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    year = info[0]
    month = months[info[1]]
    weekday = weekdays[info[6]]
    day = info[2]
    hour = info[3]
    minute = info[4]
    second = info[5]

    #return "Fri Jan 10 09:01:01 2020 time={:.1}ms TTL=1"
    return "{} {} {} {:2d}:{:2d}:{:2d} {}".format(weekday,month,day,hour,minute,second,year)

# ping function
def ping(IP, ping_num):
    global packet_size
    global server_port
    try:
        sleep(0.8)
        # create client socket
        client_socket = socket(AF_INET, SOCK_DGRAM)

        # create message
        # message = "Ping {} Fri Jan 10 09:00:00 2020".format(ping_num)
        message = "HEY"

        # send ping to server
        start_time = clock()
        client_socket.sendto(message.encode(), (IP, int(server_port)))

        # receive ping from server
        recv_message, server_address = client_socket.recvfrom(packet_size)

        # time
        end_time = clock()
        time_elapsed = (end_time - start_time)*1000

        # create success message
        success_message = "Reply from {}: Ping {} {} time={:.1f}ms TTL=1".format(server_address[0], ping_num, create_timestamp(), time_elapsed)

        # print success message and close socket
        print(success_message)
        client_socket.close()

        # return success
        return True, time_elapsed

    except:
        # timeout or disconnect
        print("Request timed out.")
        return False, 0

######################### MAIN ##################################
#   calculates ping statistics and prints them to the terminal  #
#################################################################

if(__name__ == "__main__"):
    total_successes = 0
    times = []

    print("Pinging {}:".format(server_ip))

    # iterate pings
    for i in range(ping_count):
        success, time_elapsed = ping(server_ip, i+1)

        if(success):
            # add time elapsed and success count
            total_successes += 1
            times.append(time_elapsed)

    # statistics for packets lost
    if(times == []):
        pmin = 0.0
        pmax = 0.0
        pavg = 0.0
    else:
        # compute statistics
        pmin = min(times)
        pmax = max(times)
        pavg = float(sum(times))/float(total_successes)

    # ping statistics
    output_lines = ["Ping statistics for {}:".format(server_ip), "        Segments: Sent: {}, Received: {}, Lost: {} ({}% Loss)".format(ping_count, total_successes, ping_count - total_successes, float(ping_count - total_successes)/ping_count*100), "Approximate round trip times in ms:", "        Minimum = {:.1f}ms, Maximum = {:.1f}ms, Average = {:0.1f}ms".format(float(pmin), float(pmax), float(pavg))]
    for line in output_lines:
        print(line)
