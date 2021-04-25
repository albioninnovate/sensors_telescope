#!/home/pi/Python-3.8.5/python


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


import asyncio
import configparser
import ast
import time

"""
This module sends a request to the server running on a Rpi.  The server returns data from ardunio_serial.py 
in a data structure dictated by bno055.ino which is running on the Ardunio and collecting data from the BNO055 board. 

this module receives a JSON object from the server and returns a dictionary.  

"""


# TODO  set the logging in client to be set when the method is called eg. to info or debug

def stat_config():
    # Read config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


# TODO put the configparseer in a method so that it is available when called as a module

async def tcp_echo_client(message):
    # ip_addr = config['ADDRESS']['ip_addr']

    # reader, writer = await asyncio.open_connection('169.254.162.167', 8888)
    reader, writer = await asyncio.open_connection('triscopepi.local', 8888)

    writer.write(message.encode())

    # n = int(config['DATA']['bytes_length'])  # number of bytes to read
    time.sleep(0.2)  # allow time for the data to be received
    # n = 1000 #  works but slow
    n = 100
    data = await reader.read(n)

    # data is received as a binary from which the dictionary must be extracted
    try:
        data_dict = ast.literal_eval(data.decode())  # extract the dictionary from the string received

    except Exception as e:
        print(e)
        data_dict = {}
    finally:
        writer.close()
    return data_dict


def main():
    stat_config()
    received = asyncio.run(tcp_echo_client('data pls, Thk you'))
    # print('received by client')
    return received


if __name__ == '__main__':
    print(main())
