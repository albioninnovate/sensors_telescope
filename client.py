import asyncio
import logging
import configparser
import ast
import requests


logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='server.log',
                    level=logging.DEBUG)

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')



async def tcp_echo_client(message):
#    reader, writer = await asyncio.open_connection(
#        '127.0.0.1', 8888)

    reader, writer = await asyncio.open_connection(
        '192.168.1.39', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    n = int(config['DATA']['characters'])
    data = await reader.read(n)
    print(f'Received: {data.decode()!r}')

    try:
        b_dict = ast.literal_eval(data.decode())  # extract the dictionary from the string received
        #print(b_dict)
        print('Euler angles : ', b_dict['Euler angle'])

        _az = b_dict['Euler angle'][0]
        _alt= b_dict['Euler angle'][1]
        
        print('Az =', _az)
        print('alt =', _alt)

        # api-endpoint 
        URL = "http://localhost:8090/api/main/view"
        
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {"az":_az, "alt": _alt}

        # sending get request and saving the response as response object 
        r = requests.post(url = URL, params = PARAMS) 

    except:
        print('Some values returned Null, not able to extract data')
        print('--')
        pass

    finally:
        print('Close the connection')
        writer.close()

asyncio.run(tcp_echo_client('Hello World!'))
