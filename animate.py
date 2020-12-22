# python_live_plot.py

from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import client
import flatten_dict
import quaternion


def get_data():
    """
    Euler angle - Az, Alt, yaw(?)
    Quaternion - 4 values

    :return:
    """
    received = client.main()

    #print('get data; ',received )

#    received = flatten_dict.main(received)

    return received

"""

structure of data from 'bunny.ino':
  
{X': '290.8125', 'y': '-2.0000', 'z': '2.8125', 'Sys_cal': '3', 'G_cal': '3', 'A_cal': '1', 'M_cal': '2'}

x - Heading (Azimuth]
y - (Altitude) 
z - Pitch (Altitude)  

 /* Board layout:
         +----------+
         |         *| RST   PITCH  ROLL  HEADING
     ADR |*        *| SCL
     INT |*        *| SDA     ^            /->
     PS1 |*        *| GND     |            |
     PS0 |*        *| 3VO     Y    Z-->    \-X
         |         *| VIN
         +----------+
  */


"""


x_values = []

az_values = []
roll_values = []
alt_values = []

index = count()


def animate(i):
    x_values.append(next(index))

    data = get_data()
    print('data ;', data)

    az_values.append(float(data['X']))
    roll_values.append(float(data['z']))
    alt_values.append(float(data['y']))

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
