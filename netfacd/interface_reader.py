#!/usr/bin/env python3

import netifaces

adapter = 0

def just_ip():

    print((netifaces.ifaddresses(adapter)[netifaces.AF_INET])[0]['addr'])

def just_mac():

    print((netifaces.ifaddresses(adapter)[netifaces.AF_LINK])[0]['addr'])

print("Below are available adapters")

print(netifaces.interfaces())

print("Please enter the name of an adapter if you'd like to see specific information about the adapter.")

print("If not, simply hit enter.")

adapter_name = input(">>> ")

if len(adapter_name) > 0:

    adapter = adapter_name.lower().strip()

    ip_or_mac = input("Do you want IP address or MAC address? Type ip or mac. >>> ")

    if ip_or_mac == "ip":
        
        just_ip()
    
    if ip_or_mac == "mac":

        just_mac()

else:

    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try:
            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message



