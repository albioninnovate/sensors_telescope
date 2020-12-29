# python_live_plot.py

from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import client
from utils import quaternion
import csv

import logging

log_file = 'animate.log'

logging.basicConfig(format='%(asctime)s %(lineno)d %(message)s',
                    filename=log_file,
                    level=logging.DEBUG)




"""

structure of data from 'bno055.ino':

Euler values data structure:
{X': '290.8125', 'y': '-2.0000', 'z': '2.8125', 'Sys_cal': '3', 'G_cal': '3', 'A_cal': '1', 'M_cal': '2'}

quaternion data structure: 
qW: 0.7653 qX: -0.0292 qY: -0.0126 qZ: 0.6429		Sys=3 Gyro=3 Accel=0 Mag=3

"""


def get_data():
    """
    :return:
    """
    received = client.main()
    logging.debug(received)

    #print('get data; ',received )

    return received

e_az  = []

Sys_cal = []

def animate(i):

    data = get_data()

    print(data)

    e_az.append(float(data['X']))
    Sys_cal.append(float(data['Sys_cal']))

    plt.cla()

    axs.plot(e_az,Sys_cal ,'ro')

#TODO the labels are not displaying on all three plots, only the last

fig, axs = plt.subplots(subplot_kw={'projection': 'polar'})

ani = FuncAnimation(fig, animate,1)

plt.tight_layout()
plt.show()
