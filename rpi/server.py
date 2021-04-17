#!/home/pi/Python-3.8.5


import asyncio
import logging
import configparser
#import ard_ser
import pico_ser


# TODO set this to run when the pi boots
# TODO combine the log files for server.py and ard_ser.py
#
# filename='server.log'
# level = 'logging.DEBUG'
#
# logging.basicConfig(format='%(asctime)s %(lineno)d %(message)s',
#                     filename=filename,
#                     level=level)

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')


async def handle_echo(reader, writer):

    #n = int(config['DATA']['characters'])
    n = 100
    data = await reader.read(n)

    message = data.decode()
    # logging.debug('reader read {}'.format(message) )

    #sensor = ard_ser.read(output_format='json')
    sensor = pico_ser.read(output_format='json')

    # logging.info('Read sensor')
    #print('sensor', sensor)

    data = sensor

    addr = writer.get_extra_info('peername')
    # logging.info(addr)

    print('Received', message, 'from',addr)
    #logging.info('Received', {}, 'from', addr)

    print('Send: ' , message)
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    # logging.info('Closed connection')

async def main():
#   server = await asyncio.start_server(
#       handle_echo, '192.168.1.39', 8888)

#    server = await asyncio.start_server(
#        handle_echo, 'freeside.local', 8888)
   server = await asyncio.start_server(
       handle_echo, '169.254.230.229', 8888)

   addr = server.sockets[0].getsockname()
   print('Serving on ', addr)
   # logging.info('Server started on {}'.format(addr))

   async with server:
        await server.serve_forever()

asyncio.run(main())
