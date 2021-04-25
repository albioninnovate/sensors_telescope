#!/home/pi/Python-3.8.5


import asyncio
import configparser
# import ard_ser
import pico_ser
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
    sensor = pico_ser.read(output_format='json')

    data = sensor

    # print('Received', message, 'from',addr)

    # print('Send: ' , message)
    writer.write(data)
    await writer.drain()

    # print("Close the connection")
    writer.close()


async def main():
    #   server = await asyncio.start_server(
    #       handle_echo, '192.168.1.39', 8888)

    #   server = await asyncio.start_server(
    #       handle_echo, '169.254.230.229', 8888)

    server = await asyncio.start_server(
        handle_echo, '169.254.162.167', 8888)

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
