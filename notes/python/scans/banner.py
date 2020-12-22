#!/usr/bin/python

from socket import *

def retBanner(ip, port):
    try:
        setdefaulttimeout(2)
        sock = socket()
        sock.connect((ip, port))
        banner = sock.recv(1024)
        return banner
    except:
        return

def main():
    # port = 22
    ip = "192.168.1.254"
    for port in range(1, 1000):
        banner = retBanner(ip, port)
        if banner:
                print("[+]" + ip + ": " + banner)

main()

if __name__ == '__main__':
    main()