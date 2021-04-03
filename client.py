#!/home/pi/Python-3.8.5/python


import asyncio
import logging
import configparser
import ast
import pprint
import time

"""
This module sends a request to the server running on a Rpi.  The server returns data from ardunio_serial.py 
in a data structure dictated by bno055.ino which is running on the Ardunio and collecting data from the BNO055 board. 

this module receives a JSON object from the server and returns a dictionary.  

"""


def start_logging():
    logging.basicConfig(format='%(asctime)s %(lineno)d %(message)s',
                        filename='client.log',
                        level=logging.DEBUG)

#TODO  set the logging in client to be set when the method is called eg. to info or debug

def stat_config():
    # Read config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

#TODO put the configparseer in a method so that it is avaiable when called as a module

async def tcp_echo_client(message):

    #ip_addr = config['ADDRESS']['ip_addr']
   # reader, writer = await asyncio.open_connection( '192.168.1.41', 8888)
    reader, writer = await asyncio.open_connection('10.0.252.60', 8888)
    logging.debug('create reader and writer')

    #print(f'Send: {message!r}')
    writer.write(message.encode())
    logging.info('writer : {}'.format(message))

    #n = int(config['DATA']['bytes_length'])  # number of bytes to read
    time.sleep(1)  # allow time for the data to be received
    data = await reader.read(1000)

    logging.debug('data received : {}' .format(data.decode))


# data is received as a binary from which the dictionary must be extracted
    try:
        data_dict = ast.literal_eval(data.decode())  # extract the dictionary from the string received

        logging.debug('data extracted : {}'.format(data_dict))

    except Exception as e:
        logging.debug(e)
        data_dict = {}


    finally:
        writer.close()
        logging.info('Close the connection')
    return data_dict


def main():
    start_logging()
    stat_config()
    received  = asyncio.run(tcp_echo_client('data pls, Thk you'))
    #print('received by client')
    #pprint.pprint(received)
    return received

if __name__ == '__main__':
    print(main())