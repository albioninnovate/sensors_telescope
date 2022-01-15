
# Server

## Architecture choice 

TODO

## Supporting modules 

### ard_ser.py

TODO

## Sever set up


There are two approaches to launching the server at boot; systemd and crontab.

### crontab


```
crontab -e
```


Place the following text at the bottom of the file

```
@reboot sleep 30;/usr/bin/python3 /home/pi/code/sensors_triscope/rpi/server.py
```

----

### systemd


ref https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/

The intention is that the server.py module runs at boot of the RaspberryPi platform. This allows reset of the Raspberrypi-Arduino-BNO055 system to be reset with a power cycle of the Raspberrypi. The Arduino and sensor are powered by the Raspberrypi via the USB port.  

The server is at this location in the repository to allow ready maintenance: 
```
home/pi/code/sensors_telescope/raspberrypi/server.py
```

systemd is used to manage the startup process.  Systems is configured in a 'unit file'

``` 
 sudo nano /lib/systemd/system/server.service
 ```

this project uses the python3.7+ in order to access the asyncio features (TODO add reference to main README.md)


Add in the following text :
```
[Unit]
 Description=Sensors_telescope_server
 After=multi-user.target

 [Service]
 Type=idle
 ExecStart=/home/pi/Python-3.8.5/python /home/pi/code/sensors_triscope/rpi/server.py > /home/pi/code/sensors_triscope/rpi/server.log 2>&1

 [Install]
 WantedBy=multi-user.target
```

In order to store the script’s text output in a log file you can change the ExecStart line to :
```
ExecStart=/home/pi/Python-3.8.5/python home/pi/code/sensors_telescope/rpi/server.py > home/pi/code/sensors_telescope/rpi/server.log 2>&1

```


The permission on the unit file needs to be set to 644 :
```
sudo chmod 644 /lib/systemd/system/server.service
```


Configure systemd

Now the unit file has been defined we can tell systemd to start it during the boot sequence :

``` 
 sudo systemctl daemon-reload
 sudo systemctl enable server.service
 ```


Reboot the Pi and your custom service should run :

sudo reboot

The status of the server can be checked with:
 ```
 sudo systemctl status server.service
 
 sudo systemctl status /home/pi/Python-3.8.5/python home/pi/code/sensors_telescope/rpi/server.py 
 ```


### Troubleshooting 



sudo -H pip3 install serial -t /home/pi/Python-3.8.5