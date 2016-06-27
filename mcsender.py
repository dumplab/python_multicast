#!/usr/bin/python
import sys
import socket
import multiprocessing
from time import sleep
import time
from mcconfig import MULTICAST_ADDRESS,MULTICAST_PORT,MULTICAST_TTL,MULTICAST_COUNT,MULTICAST_SEND_RATE,MULTICAST_PAYLOAD

s = time.time()
rateS = 1/float(MULTICAST_SEND_RATE)
print("Sending " + str(MULTICAST_COUNT) + " UDP segments to " + str(MULTICAST_ADDRESS) + ":" + str(MULTICAST_PORT) +" every " + str(rateS) + "s")
 # create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
#send and wait
for x in range(MULTICAST_COUNT):
	sock.sendto(str(MULTICAST_PAYLOAD),(MULTICAST_ADDRESS,MULTICAST_PORT))
	sleep(rateS)
