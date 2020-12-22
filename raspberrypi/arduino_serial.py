import serial
import json

"""
This module reads from the serial port and splits the data feed the Ardunino running bno055.ino. 
bno055.ino can return all or selected parts of the data produced by the sensor.  Note both the data and structure 
being sent carefully.  

quaternion data line structure: 
qW: 0.7653 qX: -0.0292 qY: -0.0126 qZ: 0.6429		Sys=3 Gyro=3 Accel=0 Mag=3

Each line is received in the above structue from the Ardiuno. IT must be striped and put in a dictionary structure 

ref ; https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/



"""

def to_json(dict):
    return json.dumps(dict).encode('utf-8')


def read(output_format='dict'):
    cnt = 0  
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.flush()

    while cnt <=5:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                cnt += 1

        except:
           pass

        try:
            s = line

# for Euler data :
#             readings = {
#                     'X'       : s.split('X:',-1)[1].split()[0],
#                     'Y'       : s.split('Y:',-1)[1].split()[0],
#                     'Z'       : s.split('Z:',-1)[1].split()[0],
#                     'Sys_cal' : s.split('Sys:',-1)[1].split()[0],
#                     'G_cal'   : s.split('G:',-1)[1].split()[0],
#                     'A_cal'   : s.split('A:',-1)[1].split()[0],
#                     'M_cal'   : s.split('M:',-1)[1].split()[0]
#                  }
# for Quaternion data
            readings = {
                    'qW'      : s.split('qW:',-1)[1].split()[0],
                    'qX'      : s.split('qX:',-1)[1].split()[0],
                    'qY'      : s.split('qY:',-1)[1].split()[0],
                    'qZ'      : s.split('qZ:', -1)[1].split()[0],
                    'Sys_cal' : s.split('Sys=',-1)[1].split()[0],
                    'G_cal'   : s.split('Gyro=',-1)[1].split()[0],
                    'A_cal'   : s.split('Accel=',-1)[1].split()[0],
                    'M_cal'   : s.split('Mag=',-1)[1].split()[0]
                 }


        except:
            readings = {}

        if output_format=='json':
                readings = to_json(readings)


    return readings

if __name__ == '__main__':
    r = read()
    print(r)
