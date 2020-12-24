

ref: https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/arduino-code

## From AdaFruit
To connect the assembled BNO055 breakout to an Arduino Uno, follow the wiring diagram.

    Connect Vin (red wire) to the power supply, 3-5V is fine. Use the same voltage that the microcontroller logic is based off of. For most Arduinos, that is 5V
    Connect GND (black wire) to common power/data ground
    Connect the SCL (yellow wire) pin to the I2C clock SCL pin on your Arduino. On an UNO & '328 based Arduino, this is also known as A5, on a Mega it is also known as digital 21 and on a Leonardo/Micro, digital 3
    Connect the SDA (blue wire) pin to the I2C data SDA pin on your Arduino. On an UNO & '328 based Arduino, this is also known as A4, on a Mega it is also known as digital 20 and on a Leonardo/Micro, digital 2


## Arduino Nano
SCL - A5
SDA - A4
VIN - VIN
GND - GND


## Board layout:
         +----------+
         |         *| RST   PITCH  ROLL  HEADING
     ADR |*        *| SCL
     INT |*        *| SDA     ^            /->
     PS1 |*        *| GND     |            |
     PS0 |*        *| 3VO     Y    Z-->    \-X
         |         *| VIN
         +----------+
