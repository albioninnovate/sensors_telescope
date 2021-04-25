# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
    For modifications and text not covered by other licences:

    Original software Copyright (C) 2020 Ward Hills

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as published
  by the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""


import time
import board
import busio
import adafruit_bno055
import lcd_rgb

# Use these lines for I2C
bno_SDA = board.GP16
bno_SCL = board.GP17

i2c = busio.I2C(bno_SCL, bno_SDA)

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
    mnt, sec = divmod(dd * 3600, 60)
    deg, mnt = divmod(mnt, 60)
    return deg, mnt, sec


def average(snsr, n=100):
    cnt = 1

    az_list = []
    alt_list = []

    while cnt <= n:
        az_list.append(snsr.euler[0])
        alt_list.append(snsr.euler[2])
        cnt += 1

    return sum(az_list) / n, sum(alt_list) / n


def serial_out(snsr):
    print('X:', snsr.euler[0], '  Y:', snsr.euler[1], '  Z:', snsr.euler[2])


def to_dms_str(az, alt):
    m = "' "
    s = '" '

    az_dms = decdeg2dms(az)
    az_str = str(round(az_dms[0])) + " " + str(round(az_dms[1])) + m + str(az_dms[2]) + s

    alt_dms = decdeg2dms(alt)
    alt_str = str(round(alt_dms[0])) + " " + str(round(alt_dms[1])) + m + str(round(alt_dms[2], 1)) + s

    return az_str, alt_str


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

        # send the data over the serial (USB) port
        serial_out(sensor)

        # average the values before displaying
        az, alt = average(sensor)

        # Use these lines for direct, not averaged data
        # az = str(sensor.euler[0])
        # alt = str(sensor.euler[1])

        # change to deg min and sec
        az_str, alt_str = to_dms_str(az, alt)

        nl = "\n"

        # lcd_rgb.clear_screen()
        lcd_rgb.show(az_str + nl + alt_str)
