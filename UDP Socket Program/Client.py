#!usr/bin/python

# Programmers: Marco Mitic, Brian Huante Lopez
# Date: Oct 17, 2022
# Class: COMP 177
# Assignment: CA14

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP

udp_port = 1234			        # specified port to connect

msg = input("Write String Here: " )

s.sendto(bytes(msg, 'ascii'),('localhost', udp_port))		# Sending message to UDP server)

while True:
	returndata, addr = s.recvfrom(1024)
	returndata = returndata.decode('ascii')
	print(returndata)
	if returndata != None:
		break
