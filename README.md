# Sensors_telescope
Sensor package for positioning telescope, to track targets, interfacing with astronomy software (Stellerarium). 



## BNO055 Board layout and orientation:
         +----------+
         |         *| RST   PITCH  ROLL  HEADING
     ADR |*        *| SCL
     INT |*        *| SDA     ^            /->
     PS1 |*        *| GND     |            |
     PS0 |*        *| 3VO     Y    Z-->    \-X
         |         *| VIN
         +----------+


# Design

## Hardware configuration choice 

The initial strategy was to connect the BNO055 to a Raspberry Pi via I2C.  Although it was easy enough to get data from the sensor package the values were erratic.  Several approaches were taken too, speed up data collection, take larger samples followed by averaging and also to carry the data in quaternions and calculate the Euler angels in the last step. It seems the I2C connection is perhaps not fast enough to collect the useful measurements.

A second strategy it was much more successful. This was using an I2C connection via an Arduino and a USB connection between the Arduino and a Raspberry Pi.  The data return was very steady.   The demo Arduino scripts were more than sufficient to return the heading, pitch and yaw (azimuth, altitude and tilt) along with some data quality indicators. 

## Data choice 
The BNO055 outputs several times of direct measurements (Mag, Gyro, Acc, etc) and two sets of derived information, Euler Angles and Quaternions.  A quick review of literature suggests that Euler Angles can be problematic and it is best to use quaternions in any data manipulations only conversting to Euler angels in the last steps. 
This does not see to hold for the BNO055.  Initially data was erratic prompting a strategy of averaging the output.  The output is received in multi layer dictionary structures, so a utility was written to flatten the dictionary and average them (utils/flatten_dict.py).  Another utility was written to convert quaternions to Euler angels (utils/quaternion.py). 

The Euler angles output it from the sensor seem to be quite stable and correspond well with the orientation of the chip.  the decision was made to use the output from the chip directly ignoring the quaternions for now. It is worth investigating the processing done on the microprocessor of the BNO055 there appears to be some smoothing in the output data evidenced by its stability. 

When the Euler angles are sent Stellarium they must first be inverted by multiplying by -1 and then converting into radians 

## Information flow

It is anticipated that the information produced by the sensor will be used for more than one application for example; direct display at the telescope, feedback to the positioning system and sending orientation information to external programmes like Stellarium.  To accommodate this a architecture which allowed the sensor to continually produce data that could be requested by various clients.  

The system comprises a BNO055 connected by I2C to an Arduino sending data via a serial connexion to a Raspberry Pi running a simple server which is available over a IP network.   


![image](docs/arch.png)


# Ardunio setup 

ref: https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/arduino-code

an Arduno Mega was used for prototyping and in the future is a possibility for driving motors.  To connect the assembled BNO055 breakout to an Arduino

## Arduino Mega 
    SCL - 21 
    SDA - 20
    VIN - 5v
    GND - GND


for mounting on the telescope the smaller form factor of a nano has advantages. 

## Arduino Nano
    SCL - A5
    SDA - A4
    VIN - VIN
    GND - GND

see the Adafruit instructions for the necessary libraries.  The sketch is here arduino/bno055/bno055.ino.  Note the directory 'bno055' is needed by the Arduino IDE, do not remove it.

# TODO Add photos ao wiring between Arduino and sensor  boards 


