import time
import board
import busio
import adafruit_bno055
import json
import pprint

"""
reference; 
https://github.com/adafruit/Adafruit_CircuitPython_BNO055

"""

# Use these lines for I2C
def start_sensor():
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    return sensor

# User these lines for UART
# uart = busio.UART(board.TX, board.RX)
# sensor = adafruit_bno055.BNO055_UART(uart)

def read(sensor, verbose=False):
    """
    reads the values from the sensor into a dictonary.

    :param sensor:  instance of data source
    :param verbose: if True prints the resulting dictionary
    :return:
    """
    readings = {
        "temperature"           : sensor.temperature,
        "acceleration"          : sensor.acceleration,
        "magnetic"              : sensor.magnetic,
        "gyro"                  : sensor.gyro,
        "euler"                 : sensor.euler,
        "quaternion"            : sensor.quaternion,
        "linear_acceleration"   : sensor.linear_acceleration,
        "gravity"               : sensor.gravity

                }

    if verbose is True:
        pprint(readings)
    #        print("Temperature: {} degrees C".format(sensor.temperature))
    #        print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    #        print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    #        print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    #        print("Euler angle: {}".format(sensor.euler))
    #        print("Quaternion: {}".format(sensor.quaternion))
    #        print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    #        print("Gravity (m/s^2): {}".format(sensor.gravity))
    #        print()

    return readings


def average_readings(sensor, samples, quantities='all'):
    average_data = {}
    cnt = 1
    data_sum = {}

    while cnt <= samples:
        try:
            if quantities == 'all':
                data = {
                "temperature"           : sensor.temperature,
                "acceleration"          : sensor.acceleration,
                "magnetic"              : sensor.magnetic,
                "gyro"                  : sensor.gyro,
                "euler"                 : sensor.euler,
                "quaternion"            : sensor.quaternion,
                "linear_acceleration"   : sensor.linear_acceleration,
                "gravity"               : sensor.gravity
                        }

            quantities = ["temperature", "acceleration", "magnetic", "gyro", "euler", "quaternion", "linear_acceleration",
             "gravity"]

            if quantities != 'all':
                for q in list:
                    data = {'q' : sensor.+q
                            }

        except:
            print(" Provide a list of the sensors quantities to read.  Available  are: "
                  "['temperature', 'acceleration', 'magnetic', 'gyro', 'euler', "
                  "'quaternion', 'linear_acceleration', 'gravity'] use 'all' for the complete list ")

        for key in quantities:
            data_sum[key] = data_sum[key] + data[key]

    for key in quantities:
        average_data[key] = data_sum[key]/samples

    Return average_data



def to_json(dict):
    return json.dumps(dict).encode('utf-8')


def main(output_format='dict',cnt=0):
    try:
        sensor
    
    except NameError:
        sensor = start_sensor()

    while cnt <= 10:
        imu_data = read(sensor, verbose=False)

        #print('original sensor output')
        #pprint.pprint(imu_data)

        if output_format=='json':
            imu_data = to_json(imu_data)

        #print('returned sensor output')
        #pprint.pprint(imu_data)

        cnt += 1

    time.sleep(0.1)
    return imu_data

if __name__ == '__main__':
    sensor = start_sensor()

    while True:
        imu_data = read(sensor, verbose=False)
        #pprint.pprint(imu_data)
        #print("---")
        time.sleep(1)

