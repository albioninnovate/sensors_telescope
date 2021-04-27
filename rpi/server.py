#!/home/pi/Python-3.8.5


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
# import ard_ser
import pico_svr
import socket

# TODO set this to run when the pi boots
#

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')


async def handle_echo(reader, writer):
    # n = int(config['DATA']['characters'])
    n = 1000
    data = await reader.read(n)

    # logging.debug('reader read {}'.format(message) )

    # sensor = ard_ser.read(output_format='json')
    sensor = pico_svr.read(output_format='json')

    data = sensor

    # print('Received', message, 'from',addr)

    # print('Send: ' , message)
    writer.write(data)
    await writer.drain()

    # print("Close the connection")
    writer.close()


async def main():

#    server = await asyncio.start_server(
#        handle_echo, '169.254.162.167', 8888)

    server = await asyncio.start_server(
        handle_echo, 'triscopepi.local', 8888)

    # TODO change the IP address to host name

    #    hostname = socket.gethostname()
    #    print(hostname)
    #    ipaddr = socket.gethostbyname(hostname+'.local')
    # ipaddr = socket.gethostbyname(hostname)
    #    print(ipaddr)

    # server = await asyncio.start_server(
    #    handle_echo, ipaddr, 8888)

    addr = server.sockets[0].getsockname()
    print('Serving on ', addr)

    async with server:
        await server.serve_forever()


asyncio.run(main())
