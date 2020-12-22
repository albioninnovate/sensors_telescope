# sensors_telescope
Sensor package for positioning telescope, to track targets, interfacing with astronomy software (Stellerarium). 

Notes on hardware configuration 

The initial strategy was to connect the BNO055 to a Raspberry Pi via I2C.  Although it was easy enough to get data from the sensor package the values were erratic.  Several approaches were taken too, speed up data collection, take larger samples followed by averaging and also to carry the data in quaternions and calculate the Euler angels in the last step. It seems the I2C connection is perhaps not fast enough to collect the useful measurements.

A second strategy it was much more successful. This was using an I2C connection via an Arduino and a USB connection between the Arduino and a Raspberry Pi.  The data return was very steady.   The demo Arduino scripts were more than sufficient to return the heading, pitch and yaw (azimuth, altitude and tilt) along with some data quality indicators. 



