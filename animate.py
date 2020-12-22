# python_live_plot.py

from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import client
import flatten_dict
import quaternion


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

#    received = flatten_dict.main(received)

    return received



x_values = []

az_values = []
roll_values = []
alt_values = []

index = count()


def animate(i):
    x_values.append(next(index))

    data = get_data()


    qW = float(data['qW'])
    qX = float(data['qX'])
    qY = float(data['qY'])
    qZ = float(data['qZ'])

    angles = quaternion.to_euler(qW, qX, qY, qZ)

    print('data =  ', data)

    az_values.append(float(angles[0]))
    roll_values.append(float(angles[1]))
    alt_values.append(float(angles[2]))

    plt.cla()

    axs[0].plot(x_values, az_values)
    plt.ylabel('Az')

    axs[1].plot(x_values, roll_values)
    plt.ylabel('Roll')

    axs[2].plot(x_values, alt_values)
    plt.ylabel('Alt')

#TODO the labels are not displaying on all three plots, only the last

fig, axs = plt.subplots(3)


ani = FuncAnimation(fig, animate, 1000)


plt.tight_layout()
plt.show()
