


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import client
import math


def get_data():
    """
    :return:
    """
    received = client.main()

    return received

e_az  = []
e_alt = []
Sys_cal = []

def animate(i):

    data = get_data()
    #print(data)

    e_az_new = float(data['X'])
    e_alt_new = float(data['Z'])

    # The plot will use the calibration value as the vector length in the polar plot.  In the circuit python version of
    # pico_ser.py, running the on the, PICO board does not return thee calibration value.

    if data['Sys_cal'] is None:          # this will be the case util circuitpython surfaces the calibrations values
        Sys_cal_new = 3
    else:
        Sys_cal_new = float(data['Sys_cal'])

    print(data['X'],
          " , ",
          data['Z']
          )

    e_az_new = math.radians(e_az_new)
    e_alt_new = math.radians((e_alt_new))  * -1

    # Add the new point to the list
    e_az.append(e_az_new )
    e_alt.append(e_alt_new)
    Sys_cal.append(Sys_cal_new )

    # Take the last few points to plot
    N = 5
    az = e_az[-N:]
    alt = e_alt[-N:]
    S = Sys_cal[-N:]

    axs[0].set_rmax(3)
    axs[0].set_rticks([2])
    axs[0].set_facecolor(plt.cm.gray(.95))
    axs[0].grid(True)

    axs[1].set_rticks([2])
    axs[1].set_facecolor(plt.cm.gray(.95))
    axs[1].grid(True)

    # Clear the old points from the plot
    axs[0].cla()
    axs[1].cla()

    axs[0].set_title('AZ')
    axs[1].set_title('Alt', va='bottom')


    # rotate the axes to match a compass
    axs[0].set_theta_zero_location('N')
    axs[0].set_theta_direction(-1)

    #S = [3,3,3,3]
    print(az)
    axs[0].plot(az, S, 'go')
    axs[1].plot(alt, S, 'ro')


fig, axs = plt.subplots(1,2, subplot_kw={'projection': 'polar'})


ani = FuncAnimation(fig, animate,1)

plt.tight_layout()
plt.show()
