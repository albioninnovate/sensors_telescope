# python_live_plot.py

from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import client
from utils import quaternion
import csv

import logging



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
    # logging.debug(received)

    # print('get data; ',received )

    return received


x_values = []

q_az = []
q_rol = []
q_alt = []

e_az = []
e_rol = []
e_alt = []

Sys_cal = []
G_cal = []
A_cal = []
M_cal = []

index = count()


def animate():
    x_values.append(next(index))

    data = get_data()

    print(data)

    qW = float(data['qW'])
    qX = float(data['qX'])
    qY = float(data['qY'])
    qZ = float(data['qZ'])

    q_angles = quaternion.to_euler(qW, qX, qY, qZ)

    q_az.append(float(q_angles[0]))
    q_rol.append(float(q_angles[1]))
    q_alt.append(float(q_angles[2]))

    e_az.append(float(data['X']))
    e_rol.append(float(data['Y']))
    e_alt.append(float(data['Z']))

    #    Sys = 0   Gyro = 3 Accel = 0 Mag = 0

    Sys_cal.append(float(data['Sys_cal']))
    G_cal.append(float(data['G_cal']))
    A_cal.append(float(data['A_cal']))
    M_cal.append(float(data['M_cal']))

    plt.cla()

    axs[0].plot(x_values, q_az, '-g', linewidth=1)
    axs[0].plot(x_values, e_az, '--c')
    plt.ylabel('Az')

    axs[1].plot(x_values, q_rol, '-g', linewidth=1)
    axs[1].plot(x_values, e_rol, '--c')
    plt.ylabel('Roll')

    axs[2].plot(x_values, q_alt, '-g', linewidth=1)
    axs[2].plot(x_values, e_alt, '--c')
    plt.ylabel('Alt')

    axs[3].plot(x_values, Sys_cal)
    axs[3].plot(x_values, G_cal)
    axs[3].plot(x_values, A_cal)
    axs[3].plot(x_values, M_cal)
    plt.ylabel('Cal')


# TODO the labels are not displaying on all three plots, only the last

fig, axs = plt.subplots(4)

ani = FuncAnimation(fig, animate, 1000)

plt.tight_layout()
plt.show()
