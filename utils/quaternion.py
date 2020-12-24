import numpy as np
import math as m

"""
ref https://stackoverflow.com/questions/56207448/efficient-quaternions-to-euler-transformation

"""

def to_euler(w, x, y, z):
    ysqr = y * y

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + ysqr)
    X = np.degrees(np.arctan2(t0, t1))

    t2 = +2.0 * (w * y - z * x)

    t2 = np.clip(t2, a_min=-1.0, a_max=1.0)
    Y = np.degrees(np.arcsin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (ysqr + z * z)
    Z = np.degrees(np.arctan2(t3, t4))

# A second method using ffthe maths library
# ref https://www.meccanismocomplesso.org/en/hamiltons-quaternions-and-3d-rotation-with-python/

    # t0 = 2 * (w * x + y * z)
    # t1 = 1 - 2 * (x * x + y * y)
    # X = m.atan2(t0, t1)
    #
    # t2 = 2 * (w * y - z * x)
    # t2 = 1 if t2 > 1 else t2
    # t2 = -1 if t2 < -1 else t2
    # Y = m.asin(t2)
    #
    # t3 = 2 * (w * z + x * y)
    # t4 = 1 - 2 * (y * y + z * z)
    # Z = m.atan2(t3, t4)


    return X, Y, Z

def quaternion_to_euler(w, x, y, z):


        return X, Y, Z


if __name__ == '__main__':
    to_euler(w, x, y, z)