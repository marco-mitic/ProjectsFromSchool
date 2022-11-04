#!usr/bin/python

# Programmers: Marco Mitic, Brian Huante Lopez
# Date: Oct 17, 2022
# Class: COMP 177
# Assignment: CA14

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP

udp_host = 'localhost'		        	# Host IP
udp_port = 1234			                # specified port to connect

#print type(sock) ============> 'type' can be used to see type 
				# of any variable ('sock' here)

s.bind((udp_host,udp_port))

while True:
	print("Waiting for client...")
	data, addr = s.recvfrom(1024)	        #receive data from client
	reverseString = data.upper()
	s.sendto(reverseString, addr)

