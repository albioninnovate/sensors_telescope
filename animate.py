# python_live_plot.py

import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import client



def get_data():
    """
    Euler angle - Az, Alt, yaw(?)
    Quaternion - 4 values

    :return:
    """

    received = client.main()
    # print('Euler angles : ', received['Euler angle'])
    # az = received['Euler angle'][0]
    # q1 = received['Quaternion'][1]
    return received

def condition_data(quantity,component, samples=5,):
    print(quantity)
    measurements = []
    cnt = 1

    while cnt<= samples:
        try:
            measurement  = get_data()[quantity][component]
            measurements.append(measurement)
            cnt += 1
        except KeyError:
            pass

    data_ave = sum(measurements)/samples


    return data_ave




plt.style.use('fivethirtyeight')

x_values = []
y_values = []

index = count()


def animate(i):
    x_values.append(next(index))

    #y_new = get_data()['Quaternion'][1]
    y_new = condition_data("Quaternion",1)
    #y_new = abs(y_new)
    y_values.append(y_new)
    print(y_new)
    plt.cla()
    plt.plot(x_values, y_values)


ani = FuncAnimation(plt.gcf(), animate, 1000)


plt.tight_layout()
plt.show()
