# Dylan Brett (100933134)
# TPRG-2131-02
# Nov 30, 2024
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s). I havent used any
# code from other sources other than referncing the course material


# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/

import socket
import os, time
import json

s = socket.socket()
host = '10.0.0.178' # Localhost (server IP)
port = 5000

s.bind((host, port))
s.listen(5)
print("server active") # displays if the server has been turned on


def RPi_temp():
    '''
    This def gets the Temperature of the RPis core
    '''
    #gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
    core = os.popen('vcgencmd measure_temp').readline() #gets from the os, using vcgencmd - the core-temperature
    core_temp = core.strip('temp=') # remove unwanted text using .strip
    return core_temp

def RPi_volts():
    '''
    This def gets the Voltage of the RPis core
    '''
    # ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
    volts = os.popen('vcgencmd measure_volts core').readline() #gets from the os, using vcgencmd
    core_volts = volts.strip('volt=') # remove unwanted text using .strip
    return core_volts

def Core_clock():
    '''
    This def gets the Clock speed of the RPis core
    '''
    # ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
    clock = os.popen('vcgencmd measure_clock arm').readline() #gets from the os, using vcgencmd
    core_clock = clock.strip('clock=') # remove unwanted text using .strip
    return core_clock

def Gpu_core():
    '''
    This def gets the GPU clock speed of the RPis core
    '''
    # ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
    Gpu = os.popen('vcgencmd measure_clock core').readline() #gets from the os, using vcgencmd
    Gpu_core = Gpu.strip('clock=') # remove unwanted text using .strip
    return Gpu_core

def VideoCore_voltage():
    '''
    This def gets the Video Core Voltage of the RPis core
    '''
    # ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
    video = os.popen('vcgencmd measure_volts core').readline() #gets from the os, using vcgencmd
    video_voltage = video.strip('volt=') # remove unwanted text using .strip
    return video_voltage

# loop to keep connecting to clients
while True:
    # try and except to see if the client disconnects
    try:
        c, addr = s.accept()
        print ('Got connection from',addr)
        
        # loop to keep sending data
        while True:
            # real time values of server
            core = RPi_temp()
            volts = RPi_volts()
            core_clock = Core_clock()
            Gpu_clock = Gpu_core()
            video_voltage = VideoCore_voltage()
            
            # dictionary for the real time values (with a key and its value)  
            jsonResult = {"Temperature": core, "Voltage": volts, "core-clock": core_clock, "GPU-Clock": Gpu_clock, "Video-voltage": video_voltage}
            jsonResult = json.dumps(jsonResult) # used to serialize the Python object and write it to the JSON file
            jsonbyte = bytes(jsonResult, "utf-8") # encodes the data (send as bytes)
            c.send(jsonbyte) # sends data as a byte type
            time.sleep(1) # used to slow down or speed up the data being sent
            #print(jsonbyte) # optional printout to see data flow (i used it for testing(logging))
            
    except ConnectionResetError: # if the client disconnects then the program will stop sending data
        print("the client has disconnected")
        c.close()
    except KeyboardInterrupt: # press ctrl-c to exit the program
        print("")
        print("Server Shutting down")
        c.close()
        exit(1)

