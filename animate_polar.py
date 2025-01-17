"""
    For modifications and text not covered by other licences:

    Original software Copyright (C) 2020 Ward Hills

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as published
  by the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import math

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import client


def get_data():
    """
    :return:
    """
    received = client.main()

    return received


e_az = []
e_alt = []
Sys_cal = []


# noinspection PyPep8Naming
def animate(i):
    try:
        data = get_data()

        # The plot will use the calibration value as the vector length in the polar plot.
        # In the circuitpython version of pico_svr.py does not return the calibration value.

        if len(data) <= 3:  # this will be the case until circuitpython surfaces the calibrations values
            Sys_cal_new = 3
        else:
            Sys_cal_new = float(data['Sys_cal'])
    except:
        print('data not received')

    e_az_new = float(data['X'])
   # e_alt_new = float(data['Z'])

    #if sensor is 'reverse mounted'
    e_alt_new = float(data['Z'])  * -1

    e_az_new = math.radians(e_az_new)
    e_alt_new = math.radians(e_alt_new)

    # Add the new point to the list
    e_az.append(e_az_new)
    e_alt.append(e_alt_new)
    Sys_cal.append(Sys_cal_new)

    # Take the last few points to plot
    N = 5
    az = e_az[-N:]
    alt = e_alt[-N:]
    S = Sys_cal[-N:]

    axs[0].set_rmax(3)
    axs[0].set_rticks([1, 2, 3])

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

    axs[0].plot(az, S, 'go')
    axs[1].plot(alt, S, 'ro')

    axs[0].text(0, 0,
                round(math.degrees(e_az_new), 2),
                bbox=dict(facecolor='white', edgecolor='green', alpha=0.8),
                fontsize=24,
                ha='center',
                va='center'
                )

    axs[1].text(0, 0,
                round(math.degrees(e_alt_new), 2),
                bbox=dict(facecolor='white', edgecolor='red', alpha=0.8),
                fontsize=24,
                ha='center',
                va='center'
                )


fig, axs = plt.subplots(1, 2, subplot_kw={'projection': 'polar'})

ani = FuncAnimation(fig, animate, 1)

plt.tight_layout()
plt.show()
