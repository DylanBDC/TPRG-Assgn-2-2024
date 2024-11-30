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

# Runs on PC, directly from Thonny
# The client
print("The client")


s = socket.socket()
host = '10.0.0.178'  # ip of raspberry PI, running the server
port = 5000
s.connect((host, port))


encoded_string = s.recv(1024)
#data = encoded_string.decode('utf-8')
data = json.loads(encoded_string) # json.loads decodes the JSON string into a python object
core = data['Temperature'] # access the temp using the temperature key in the data dictionarry 
volts = data['Voltage'] # access voltage in data
print(encoded_string)
print("Core Temperature:", core)
print("Core Voltage", volts)
        

s.close()
    
