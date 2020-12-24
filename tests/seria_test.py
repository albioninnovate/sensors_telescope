
import serial

if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    except:
        ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ser.flush()

    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
        except:
           pass
