# Programmers: Brian Huante Lopez, Marco Mitic
# Class: COMP 177
# Assignment: Project 2
# Date: October 30, 2022

# Usage: sudo python traceroute.py [ip address of host]

# Description:
# Program does a real time traceroute to host address, up to ttl of 20
# Program only accepts an IP address as an argument to reach host
# The program finishes when host address is reached or ICMP Port is unreachable
# Program displays each hop of the traceroute
# If hop has no response, displays *
# If hop has a response, displays discovered IP address


from scapy.all import *
import sys
import random
import ipaddress

from scapy.layers.inet import IP, UDP


def traceroute():
    n = len(sys.argv)
    # program will only run if we have a minimum of 2 command line arguments
    if n == 2:
        sys.exit("Too few/many arguments.")

    # Check to see if argument passed is an IP address
    try:
        ipaddress.ip_address(sys.argv[1])
    except ValueError:
        print("Not an IP address to reach host".format(sys.argv[1]))
        quit()

    for i in range(1, 21):
        host_ip = sys.argv[1]
        # Destination port number
        dport_num = random.randrange(33434, 33464)
        # Source port number
        sport_num = random.randrange(33434, 33464)

        pkt = IP(dst=host_ip, ttl=i) / UDP(dport=dport_num, sport=sport_num)
        reply = sr1(pkt, verbose=0, timeout=3)

        if reply is None:
            # If reply is none, continue on with next packet
            print("%d.\t\t*" % i)
        elif reply.type == 3:
            # Reached destination, break out of for loop and end program
            print("%d.\t\t" % i, reply.src)
            break
        elif reply.code == 3:
            # Destination port unreachable, break out of for loop and end program
            print("%d.\t\tDestination port unreachable" % i)
            break
        else:
            # Display what hop we are on and discovered IP address
            print("%d.\t\t" % i, reply.src)


if __name__ == '__main__':
    conf.verb = 0
    traceroute()
