# Dylan Brett (100933134)
# TPRG-2131-02
# Nov 25, 2024
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s). I havent used any
# code from other sources other than referncing the course material

import socket

Runs on PC, directly from Thonny
The client
print("The client")

for x in range(6):
    s = socket.socket()
    host = '192.168.10.111'  # ip of raspberry PI, running the server
    port = 5000
    s.connect((host, port))
    print(s.recv(1024))
    s.close()
    