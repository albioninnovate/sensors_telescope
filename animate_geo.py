# python_live_plot.py

import math

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import client

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


e_az = []
e_alt = []
Sys_cal = []


def animate():
    data = get_data()

    e_az_new = float(data['X'])
    e_alt_new = float(data['Z'])
    Sys_cal_new = float(data['Sys_cal'])

    print(data['X'],
          " , ",
          data['Z'],
          " , ",
          data['Sys_cal']
          )

    e_az_new = math.radians(e_az_new)
    e_alt_new = math.radians(e_alt_new) * -1

    # Add the new point to the list
    e_az.append(e_az_new)
    e_alt.append(e_alt_new)
    Sys_cal.append(Sys_cal_new)

    # Take the last few points to plot
    N = 5
    az = e_az[-N:]
    alt = e_alt[-N:]

    # axs[0].set_rmax(3)
    # axs[0].set_rticks([2])
    # axs[0].set_facecolor(plt.cm.gray(.95))
    # axs[0].grid(True)

    #
    # axs[1].set_rticks([2])
    # axs[1].set_facecolor(plt.cm.gray(.95))
    # axs[1].grid(True)
    #
    # # Clear the old points from the plot
    # axs[0].cla()
    # axs[1].cla()
    #
    # axs[0].set_title('AZ')
    # axs[1].set_title('Alt', va='bottom')
    #
    #
    # # rotate the axes to match a compass
    # axs[0].set_theta_zero_location('N')
    # axs[0].set_theta_direction(-1)

    axs.plot(az, alt, 'go')


# TODO the labels are not displaying on all three plots, only the last

fig, axs = plt.subplots(111, subplot_kw={'projection': "hammer"})

ani = FuncAnimation(fig, animate, 1)

plt.tight_layout()
plt.show()
