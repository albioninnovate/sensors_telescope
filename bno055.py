import time
import board
import busio
import adafruit_bno055
import json
import pprint

# Use these lines for I2C
def start_sensor():
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    return sensor

# User these lines for UART
# uart = busio.UART(board.TX, board.RX)
# sensor = adafruit_bno055.BNO055_UART(uart)

def read(sensor, verbose=True):
    readings = {
        "Temperature"           : sensor.temperature,
        "Accelerometer"         : sensor.acceleration,
        "Magnetometer"          : sensor.magnetic,
        "Gyroscope"             : sensor.gyro,
        "Euler angle"           : sensor.euler,
        "Quaternion"            : sensor.quaternion,
        "Linear acceleration"   : sensor.linear_acceleration,
        "Gravity"               : sensor.gravity

                }

    if verbose is True:
        print("Temperature: {} degrees C".format(sensor.temperature))
        print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
        print("Magnetometer (microteslas): {}".format(sensor.magnetic))
        print("Gyroscope (rad/sec): {}".format(sensor.gyro))
        print("Euler angle: {}".format(sensor.euler))
        print("Quaternion: {}".format(sensor.quaternion))
        print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
        print("Gravity (m/s^2): {}".format(sensor.gravity))
        print()

    return readings

def to_json(dict):
    return json.dumps(dict).encode('utf-8')


def main(output_format='dict'):
    sensor = start_sensor()

    imu_data = read(sensor, verbose=False)

    pprint.pprint(imu_data) 

    if output_format=='json':
        imu_data = to_json(imu_data)


    pprint.pprint(imu_data)
    return imu_data

if __name__ == '__main__':
    sensor = start_sensor()
    while True:
        imu_data = read(sensor, verbose=False)

        pprint.pprint(imu_data) 

        imu_data = to_json(imu_data)

        pprint.pprint(imu_data)

        time.sleep(1)
