import serial
import json

"""
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

            readings = {
                    'X'       : s.split('X:',-1)[1].split()[0],
                    'y'       : s.split('Y:',-1)[1].split()[0],
                    'z'       : s.split('Z:',-1)[1].split()[0],
                    'Sys_cal' : s.split('Sys:',-1)[1].split()[0],
                    'G_cal'   : s.split('G:',-1)[1].split()[0],
                    'A_cal'   : s.split('A:',-1)[1].split()[0],
                    'M_cal'   : s.split('M:',-1)[1].split()[0]
                 }


        except:
            readings = {}

        if output_format=='json':
                readings = to_json(readings)


    return readings

if __name__ == '__main__':
    r = read()
    print(r)
