import adafruit_bno055
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

print('i2c :', i2c)

sensor = adafruit_bno055.BNO055_I2C(i2c)

print(sensor)

