

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
import pprint
import requests
import client_pico_bno
import client


def get_status(propId=-2, actionId=-2, verbose=False):
    try:
        URL = "http://localhost:8090/api/main/status"

        PARAMS = {"propId": propId, "actionId": actionId}

        status = requests.get(url=URL, params=PARAMS)

        if verbose:
            print(URL)
            print(PARAMS)
            pprint.pprint(status.json())

        return status.json()

    except Exception:
        # print(e)
        print("Is Stellarium running with the remote control plugin?")


"""
ref https://stellarium.org/doc/head/remoteControlApi.html

Launch Stellarium Application 
go to 
	1. Configuration Menu (F2)
	2. plug-in
Select Remote Control plug-in
	Options - launch at startup

Restart Stellarium Application to load plug-in

Return to the Remote Control plug-in
		Click the Configure button 
		Check the Server enabled box
				Returns: listening on 127.0.1.1
		Confirm: Port number: 8096
		Check the Enable automatically at start up box
		Save settings 
"""

def send_altaz(_az=0, _alt=0):
    """

    :_az   In radians
    :_alt  In radians
    :return:
    """

    # api-endpoint
    URL = "http://localhost:8090/api/main/view"

    # az and alt must be given in radians.
    # -1 to correct for differences in the coor system

    # defining a params dict for the
    # parameters to be sent to the API
    PARAMS = {"az": _az, "alt": _alt}

    # sending get request and saving the response as response object
    r = requests.post(url=URL, params=PARAMS)
    return r


def send_fov(fov=20):
    URL = "http://localhost:8090/api/main/fov"
    r = requests.post(url=URL, params={"fov": fov})
    return r


if __name__ == '__main__':
    propId = 1
    actionId = 1
    s = get_status(propId, actionId, verbose=False)
    # pprint.pprint(s)

    # print('J Day :', s['time']['jday'])

    while True:
       # received = client.main()
        received = client_pico_bno.main()
        # print('Euler angles : ', received['Euler angle'])

        # az = float(received['X'])
        # alt = float(received['Z'])

        az = float(received[0])
    #    alt = float(received[2])

        # if sensor is 'reverse' mounted
        alt = float(received[2])  * -1

        #az_rad = - math.radians(az) - math.pi
#        az_rad = - math.radians(az)
        az_rad = - (math.radians(az) ) -math.pi
        alt_rad = math.radians(alt)

       # print("Az/Alt : ", az_rad, ' / ', alt_rad)

        x = 0
        while x <= 1:
            send_altaz(az_rad, alt_rad)
#            send_fov(40)
            x += 1
