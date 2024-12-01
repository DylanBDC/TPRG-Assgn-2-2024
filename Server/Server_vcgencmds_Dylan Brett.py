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
host = '10.0.0.178' # Localhost
port = 5000

s.bind((host, port))
s.listen(5)
print("server active")
pass




def RPi_temp():

    #gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
    #t = os.popen('vcgencmd measure_volts ain1').readline() #gets from the os, using vcgencmd - the core-temperature
    core = os.popen('vcgencmd measure_temp').readline()
    core_temp = core.strip('temp=')
    # initialising json object string
    #ini_string = {"Temperature": core}
    #ini_string = json.dumps(ini_string)
    #jsonbyte = bytes(ini_string, "UTF-8")
    # converting string to json
    #f_dict = eval(ini_string) # The eval() function evaluates JavaScript code represented as a string and returns its completion value.
    #return f_dict
    return core_temp

def RPi_volts():

    volts = os.popen('vcgencmd measure_volts core').readline()
    core_volts = volts.strip('volt=')
    #voltage = {"Core Voltage": core}
    #voltage = json.dumps(voltage)
    #jsonbytevolt = bytes(voltage, "UTF-8")
    
    return core_volts

def Core_clock():
    
    clock = os.popen('vcgencmd measure_clock arm').readline()
    core_clock = clock.strip('clock=')
    #voltage = {"Core Voltage": core}
    #voltage = json.dumps(voltage)
    #jsonbytevolt = bytes(voltage, "UTF-8")
    
    return core_clock

def Gpu_core():
    
    Gpu = os.popen('vcgencmd measure_clock core').readline()
    Gpu_core = Gpu.strip('clock=')
    #voltage = {"Core Voltage": core}
    #voltage = json.dumps(voltage)
    #jsonbytevolt = bytes(voltage, "UTF-8")
    
    return Gpu_core

def VideoCore_voltage():
    
    video = os.popen('vcgencmd measure_volts core').readline()
    video_voltage = video.strip('volt=')
    #voltage = {"Core Voltage": core}
    #voltage = json.dumps(voltage)
    #jsonbytevolt = bytes(voltage, "UTF-8")
    
    return video_voltage
    


# loop to keep connecting to clients
while True:
#     c, addr = s.accept()
#     print ('Got connection from',addr)
    try:
        c, addr = s.accept()
        print ('Got connection from',addr)
        
        # loop to keep sending data
        while True:
            core = RPi_temp()
            volts = RPi_volts()
            core_clock = Core_clock()
            Gpu_clock = Gpu_core()
            video_voltage = VideoCore_voltage()
  
            jsonResult = {"Temperature": core, "Voltage": volts, "core-clock": core_clock, "GPU-Clock": Gpu_clock, "Video-voltage": video_voltage}
            jsonResult = json.dumps(jsonResult) # used to serialize the Python object and write it to the JSON file
            jsonbyte = bytearray(jsonResult, "utf-8")
            #res = bytes(str(RPi_temp()), 'utf-8') # needs to be a byte
            c.send(jsonbyte) # sends data as a byte type
            time.sleep(1)
            #print(jsonbyte) # optional printout to see data flow (i used it for logging)
            #c.send(volts())
            #c.close()
    except ConnectionResetError:
        print("the client has disconnected")
        c.close()
    except KeyboardInterrupt:
        print("")
        print("Server Shutting down")
        c.close()
        exit(1)

