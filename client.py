#!/usr/bin/env python

# client.py  
import socket, pytz

# get local machine name
host = "127.0.1.1"
port = 50000

print("\nLIST OF PYTZ TIMEZONES: \n")
for tz in pytz.all_timezones:
    print tz
print("\nEND OF LIST\n")

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# connection to hostname on the port.
s.connect((host, port))
                              
while 1:
    tz = raw_input("Timezone (or close): ")
    s.send(tz)
    if tz == 'close':
        print("Closing!")
        break
    # Receive no more than 1024 bytes
    timezone = s.recv(1024)
    print(timezone)                                     

s.close() 
