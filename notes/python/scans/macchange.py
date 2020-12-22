#!/usr/bin/python

import subprocess


def change_mac_address(interface, new_mac_address):
    subprocess.call(["ifconfig " + interface + " down"], shell=True)
    subprocess.call(["ifconfig " + interface + " hw " + "ether " + new_mac_address], shell=True)
    subprocess.call(["ifconfig " + interface + " up"], shell=True)


def main():
    interface = str(input("[*] Enter Interface To Change Mac Address On: "))
    new_mac_address = input("[*] Enter Mac Address To Change To: ")
    
    before_change = subprocess.check_output(["ifconfig " + interface], shell=True)
    change_mac_address(interface, new_mac_address)
    after_change = subprocess.check_output(["ifconfig " + interface], shell=True)

    print("before change: " + str(before_change))
    print("after change: " + str(after_change))

main()