#!/usr/bin/python

from scapy.all import *


def findDNS(p):

    try:
        if p.haslayer(DNS):
            print(p[IP].src, p[DNS].summary())
    except:
        pass


sniff(prn=findDNS)