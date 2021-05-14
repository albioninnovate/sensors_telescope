import numpy as np
#from sklearn.linear_model import LinearRegression
import datetime

from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u
from astropy.time import Time
from pprint import pprint

nav_stars = ["Polaris", "Rigel","Vega", "Pollux", "Betelgeuse", "Regulus"]

def get_coor(obstime, star_name="Polaris"):

    time = Time(obstime)
    location = EarthLocation(lat=52.2265296*u.deg, lon=0.0901498*u.deg, height=52*u.m)
    target = SkyCoord.from_name(star_name)

    target_altaz = target.transform_to(AltAz(obstime=time,location=location)).to_string('decimal')

    target_az = target_altaz.split(" ")[0]
    target_alt = target_altaz.split(" ")[1]


    return [time,
            target_alt,
            target_az
            ]


#
# def linear_regression():
#     X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
#     # y = 1 * x_0 + 2 * x_1 + 3
#     y = np.dot(X, np.array([1, 2])) + 3
#     reg = LinearRegression().fit(X, y)
#     reg.score(X, y)
#
#     return reg.coef_ , reg.intercept_

def predict():
    return reg.predict(np.array([[3, 5]]))

if __name__ == '__main__':

    obstime = datetime.datetime.now()
    position_calc = {}

    for star in nav_stars:
        coor = get_coor(obstime, star)
        print(star,"  ",coor)

# if the nave star is too low it is not useful
        if float(coor[1]) >= 20:
            position_calc[star] = coor

    pprint(position_calc)