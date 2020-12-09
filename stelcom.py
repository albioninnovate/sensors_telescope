import requests
import pprint
import client

def get_status(propId=-2, actionId=-2, verbose=False):
    try:
        URL = "http://localhost:8090/api/main/status"

        PARAMS = {"propId": propId, "actionId" : actionId}

        status = requests.get(url=URL, params=PARAMS)

        if verbose == True:
            print(URL)
            print(PARAMS)
            pprint.pprint(status.json())

    except Exception as e:
        status = e

    return status.json()

# time in julian day
# location

# https://stellarium.org/doc/head/remoteControlApi.html

def send_altaz(_az=180, _alt=45):
#_az = 180
#_alt = 45

    # api-endpoint
    URL = "http://localhost:8090/api/main/view"

    # defining a params dict for the
    # parameters to be sent to the API
    PARAMS = {"az": _az, "alt": _alt}

    # sending get request and saving the response as response object
    r = requests.post(url=URL, params=PARAMS)
    return r

def send_fov(fov=5):
    URL = "http://localhost:8090/api/main/fov"
    r = requests.post(url=URL, params={"fov" : 5})
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
        az = received['Euler angle'][0]
        alt = received['Euler angle'][1]

        send_altaz(az,alt)
        send_fov()
