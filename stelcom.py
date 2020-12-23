import requests
import pprint
import client
import math

def get_status(propId=-2, actionId=-2, verbose=False):
    try:
        URL = "http://localhost:8090/api/main/status"

        PARAMS = {"propId": propId, "actionId" : actionId}

        status = requests.get(url=URL, params=PARAMS)

        if verbose == True:
            print(URL)
            print(PARAMS)
            pprint.pprint(status.json())

        return status.json()

    except Exception as e:
        #print(e)
        print("Is Stellarium running with the remote control plugin?")



# https://stellarium.org/doc/head/remoteControlApi.html

def send_altaz(_az=180, _alt=45):
#_az = 180
#_alt = 45

    # api-endpoint
    URL = "http://localhost:8090/api/main/view"

# az and alt must be given in radians.
# -1 to correct for differences in the coor system

    _az_rad = math.radians(_az * -1)
    _alt_rad = math.radians(_alt  )

    # defining a params dict for the
    # parameters to be sent to the API
    PARAMS = {"az": _az_rad, "alt": _alt_rad}

    # sending get request and saving the response as response object
    r = requests.post(url=URL, params=PARAMS)
    return r

def send_fov(fov=20):
    URL = "http://localhost:8090/api/main/fov"
    r = requests.post(url=URL, params={"fov" : fov})
    return r

if __name__ == '__main__':
    propId = 1
    actionId = 1
    s = get_status(propId, actionId, verbose=False)
    #pprint.pprint(s)

    #print('J Day :', s['time']['jday'])

    while True:
        received = client.main()
        #print('Euler angles : ', received['Euler angle'])
        az = float(received['X'])
        alt = float(received['Z'])

        x = 0
        while x <= 10:
            send_altaz(az,alt)
            send_fov(5)
            x += 1