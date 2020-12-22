#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("[*] Enter the host to scan: ")
open_ports = []

def portscanner(port):
    if sock.connect_ex((host, port)):
        print("Port {} is closed".format(port))
        #pass
    else:
        open_ports.append(port)

for port in range(0, 1000):
    portscanner(port)

print("")
print("")
print("*" * 10)
print("the following ports are open:")
print(open_ports)