#!usr/bin/python

# Programmers: Marco Mitic, Brian Huante Lopez
# Date: Oct 31, 2022
# Class: COMP 177
# Assignment: CA17

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      # For TCP

tcp_host = 'localhost'		        	# Host IP
tcp_port = 1234			                # specified port to connect

#print type(sock) ============> 'type' can be used to see type 
				# of any variable ('sock' here)

s.bind((tcp_host,tcp_port))
s.listen(1)

while True:
	print("Waiting for client...")
	cs, iptuple = s.accept()
	msg = cs.recv(1024)
	reverseString = msg.upper()
	cs.send(reverseString)
	cs.close()

