#!/usr/bin/python

import serial
import json

"""
This module reads from the serial port and splits the data feed the RasberryPi PICO running a version of pico/bno055.py in this repo 
bno055.py can return many or selected parts of the data produced by the sensor.  

Note both the data and structure being sent carefully.  

quaternion data line structure: 
qW: 0.7653 qX: -0.0292 qY: -0.0126 qZ: 0.6429		Sys=3 Gyro=3 Accel=0 Mag=3

Each line is received in the above structure from the Ardiuno. IT must be striped and put in a dictionary structure 


"""

def to_json(dict):
    return json.dumps(dict).encode('utf-8')


def read(output_format='dict'):

    """
    This module runs on the Raspberrypi. It reads binary data from the serial port. Expects data from an
    Ardunio running arduino/bno055/bno055.ino sketch. Parses the decoded data into a dictionary with expected keys.
    Optionally, the data can be converted to json for sending to a client by raspberrypi/server.py

    Baud rate is dictated by the seed of the connection with the Ardunio. The baud rates must match.


    :param output_format: dict, or json,  default is dict
    :return: data as either dict of json
    """
    
    # TODO improve the identification of the serial port

    try:
        #ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        ser = serial.Serial('/dev/ttyACM1', 115200, timeout=1)


    except:
        #ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        #ser = serial.Serial('/dev/ttyACM1', 115200, timeout=1)
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)


    ser.flush()

    while True:
        readings = {}
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                #print(line)

                s = line

                # readings = {
                         # 'X'       : s.split('X:',-1)[1].split()[0],
                         # 'Y'       : s.split('Y:',-1)[1].split()[0],
                         # 'Z'       : s.split('Z:',-1)[1].split()[0],
                        # 'qW'      : s.split('qW:',-1)[1].split()[0],
                        # 'qX'      : s.split('qX:',-1)[1].split()[0],
                        # 'qY'      : s.split('qY:',-1)[1].split()[0],
                        # 'qZ'      : s.split('qZ:', -1)[1].split()[0],
                        # 'Sys_cal' : s.split('Sys=',-1)[1].split()[0],
                        # 'G_cal'   : s.split('Gyro=',-1)[1].split()[0],
                        # 'A_cal'   : s.split('Accel=',-1)[1].split()[0],
                        # 'M_cal'   : s.split('Mag=',-1)[1].split()[0]
                 # }
                 
                 
                readings = {
                         'X'       : s.split('X:',-1)[1].split()[0],
                         'Y'       : s.split('Y:',-1)[1].split()[0],
                         'Z'       : s.split('Z:',-1)[1].split()[0]
                 }
                 
                
                if output_format == 'json':
                    #print('jason')
                    readings = to_json(readings)
            
                return readings

        except Exception as e:
            logging.debug(e)
            print(e)
            pass


if __name__ == '__main__':
    while True:
        r = read()
        print('as dict : ',r)
        
        j = read(output_format='json')
        print('as JSON :',j)
