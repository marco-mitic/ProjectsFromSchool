#!usr/bin/python

# Programmers: Marco Mitic, Brian Huante Lopez
# Date: Oct 31, 2022
# Class: COMP 177
# Assignment: CA17

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      # For TCP

tcp_port = 1234			        # specified port to connect

msg = input("Write String Here: " )

s.connect(('localhost' , tcp_port))
s.send(bytes(msg, 'ascii'))		# Sending message to TCP server)

while True:
	returndata = s.recv(1024)
	returndata = returndata.decode('ascii')
	s.close()
	print(returndata)
	if returndata is not None:
		break
