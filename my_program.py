#!/usr/bin/python3

import socket

print ("Program to check the hostname and IP of the system")
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Hostname is:" + hostname)    
print("IP Address is:" + IPAddr)  
