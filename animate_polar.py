# python_live_plot.py

from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import client
from utils import quaternion
import csv
import math





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

    return received

e_az  = []

Sys_cal = []

def animate(i):

    data = get_data()

    e_az_new = float(data['X'])
    Sys_cal_new = float(data['Sys_cal'])

    print(data['X']
          ," , ",
          data['Sys_cal']
          )

    e_az_new = math.radians(e_az_new)
    Sys_cal_new = math.radians(Sys_cal_new)

    # Add the new point to the list
    e_az.append(e_az_new )
    Sys_cal.append(Sys_cal_new )

    # Take the last few points to plot
    N = 5
    e = e_az[-N:]
    S = Sys_cal[-N:]

    plt.cla()  # Clear the ole points from the plot

    # rotate the axes to match a compass
    axs.set_theta_zero_location('N')
    axs.set_theta_direction(-1)

    axs.plot(e, S, 'ro')

#TODO the labels are not displaying on all three plots, only the last

fig, axs = plt.subplots(subplot_kw={'projection': 'polar'})

ani = FuncAnimation(fig, animate,1)

plt.tight_layout()
plt.show()
