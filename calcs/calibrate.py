import numpy as np
from sklearn.linear_model import LinearRegression
import datetime
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u
from astropy.time import Time
from pprint import pprint
import random



nav_stars = ["Polaris", "Rigel","Vega", "Pollux", "Betelgeuse", "Regulus"]

def get_coor(obstime, star_name="Polaris"):

    time = Time(obstime)
    location = EarthLocation(lat=52.2265296*u.deg, lon=0.0901498*u.deg, height=52*u.m)
    target = SkyCoord.from_name(star_name)


    target_altaz = target.transform_to(AltAz(obstime=time,location=location)).to_string('decimal')

    target_az = target_altaz.split(" ")[0]
    target_alt = target_altaz.split(" ")[1]

    #print('target :',[target_alt, target_az])

    return  [target_alt, target_az]

# def make_test_data(position_calc):
#     for key in position_calc:
#         for item in position_calc[key]:
#             if position_calc[key][]:

def linear_regression():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    # y = 1 * x_0 + 2 * x_1 + 3
    y = np.dot(X, np.array([1, 2])) + 3
    reg = LinearRegression().fit(X, y)
    reg.score(X, y)

    reg.predict(np.array([[3, 5]]))

    return reg.coef_ , reg.intercept_

def predict():
    return reg.predict(np.array([[3, 5]]))

if __name__ == '__main__':

    obstime = datetime.datetime.now().isoformat()
    position_calc = {}
    obstime_mea = {}

    for star in nav_stars:
        coor = get_coor(obstime, star)

        position_calc[star] = {obstime : [coor[0], coor[1]]}

    pprint(position_calc)

    y = []
    for star in nav_stars:
        for keys in position_calc[star]:
            y_ = position_calc[star][keys][0]
            y.append(y_)

   # print(y)

    x= []
    for sample in y:
        mea = float(sample) * (1+random.uniform(-0.1,0.1))
        x.append(mea)

    X = np.asarray(x)
    lr = LinearRegression()
    lr.fit(X.reshape(-1, 1), y)

    print(lr.predict([[39]]))



    #linear_regression()