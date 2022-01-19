# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board

#for the bno055
import busio
#import bitbangio
import adafruit_bno055

#fr the LCD
import lcd_rgb


    # Use these lines for I2C
bno_SDA = board.GP18
bno_SCL = board.GP19

i2c = busio.I2C(bno_SCL,bno_SDA)


##i2c = bitbangio.I2C(bno_SCL, bno_SDA)

sensor = adafruit_bno055.BNO055_I2C(i2c)

# User these lines for UART
# uart = busio.UART(board.TX, board.RX)
# sensor = adafruit_bno055.BNO055_UART(uart)

last_val = 0xFFFF

def temperature():
    global last_val  # pylint: disable=global-statement
    result = sensor.temperature
    if abs(result - last_val) == 128:
        result = sensor.temperature
        if abs(result - last_val) == 128:
            return 0b00111111 & result
    last_val = result
    return result


def decdeg2dms(dd):
    mnt,sec = divmod(dd*3600,60)
    deg,mnt = divmod(mnt,60)
    return deg,mnt,sec

def average(sensor, n=100):
    cnt=1

    az_list = []
    alt_list = []

    while cnt <= n:
        az_list.append(sensor.euler[0])
        alt_list.append(sensor.euler[2])
        cnt +=1
    # az_ave  = sum(az_list)/n
    # alt_ave = sum(alt_list)/n
    return sum(az_list)/n , sum(alt_list)/n

def serial_out(sensor):
    print('X:',sensor.euler[0], '  Y:',sensor.euler[1], '  Z:',sensor.euler[2])

def to_dms_str(az,alt):
    m = "' "
    s = '" '

    az_dms = decdeg2dms(az)
    az_str =  str(round(az_dms[0]))+" "+str(round(az_dms[1]))+m+str(az_dms[2])+s

    alt_dms = decdeg2dms(alt)
    alt_str =  str(round(alt_dms[0]))+" "+str(round(alt_dms[1]))+m+str(round(alt_dms[2],1))+s

    return az_str , alt_str

if __name__ == "__main__":

    while True:

#    print("Temperature: {} degrees C".format(sensor.temperature))
#    """
#    print(
#        "Temperature: {} degrees C".format(temperature())
#    )  # Uncomment if using a Raspberry Pi
#    """
#    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
#    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
#    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
#    print("Euler angle: {}".format(sensor.euler))
#    print("Quaternion: {}".format(sensor.quaternion))
#    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
#    print("Gravity (m/s^2): {}".format(sensor.gravity))
#    print()

    #send the data over the serial (USB) port
        #i2c.try_lock()
        serial_out(sensor)
        #i2c.unlock()
        #i2c.deinit()




    # average the values before displaying
        az , alt = average(sensor)
       # print(az,alt)


    #az = str(sensor.euler[0])
    #alt = str(sensor.euler[1])
    #lcd.message =az+nl+alt

#change to deg min and sec
        print(az,alt)
        az_str , alt_str = to_dms_str(az,alt)


        nl = "\n"
#    lcd.clear()

#    lcd.message =az_str+nl+alt_str
        print(az_str+nl+alt_str)
    #lcd_rgb.clear_screen()
        lcd_rgb.show(az_str+nl+alt_str)
        print(az_str+nl+alt_str)