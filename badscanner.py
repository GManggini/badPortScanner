#!/bin/python3

import sys
import socket
from datetime import datetime

#Define your target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amout of arguments. ")
	print ("Syntax: python3 badscanner.py <ip>")
	
#Add a cute banner 
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
		print("." * 3)
except KeyboardInterrupt:
	print("\nExisting program.")
	print("-" * 50)
	sys.exit()
	
except socket.gaierror:
	print("-" * 50)
	print("Hostname could not be resolved.")
	print("-" * 50)
	sys.exit()
	
except socket.error:
	print("-" * 50)
	print("Could not connect to server.")
	print("-" * 50)
	sys.exit()
	
			
			
			
			
			
			
