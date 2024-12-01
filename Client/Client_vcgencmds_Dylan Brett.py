# Dylan Brett (100933134)
# TPRG-2131-02
# Nov 30, 2024
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s). I havent used any
# code from other sources other than referncing the course material

#Cited
#https://www.datacamp.com/tutorial/json-data-python?utm_source=google&utm_medium=paid_search

import socket
import json
import time

# Runs on PC, directly from Thonny
# The client
print("The client")


s = socket.socket()
host = '10.0.0.178'  # ip of raspberry PI, running the server
port = 5000
#s.connect((host, port))

#while True:
try:
    s.connect((host, port))
    while True:
        encoded_string = s.recv(1024)
        decoded_string = encoded_string.decode('utf-8') # decode the string
        data = json.loads(decoded_string) # converts the json string into a python object
        core = data["Temperature"]
        volts = data["Voltage"]
        core_clock = data["core-clock"]
        #print(encoded_string)
        print("Core Temperature: ", core)
        print("Core Voltage: ", volts)
        print("Core Clock: ", core_clock)
        #encoded_string = b''

except socket.gaierror:
    print('error resolving host')
    #s.close()
    
except KeyboardInterrupt:
    print("client exiting...") # exit the program if ctrl-c
    
finally:
    print("lost connection")
    s.close()
    
