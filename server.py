import asyncio
#import sensor_mock
import bno055
import logging
import configparser


logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='server.log',
                    level=logging.INFO)

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')


async def handle_echo(reader, writer):
    data = await reader.read(int(config['DATA']['characters']))
    message = data.decode()

    sensor = bno055.main(output_format='json')
    logging.info('Read sensor')
    print('sensor', sensor)

    # print(type(sensor))
    # if type(sensor) == bytes is True:
    #     print('not bytes')
    #     try:
    #         data = sensor.encode()
    #     except Exception as e:
    #         print(e)
    #         pass
    # elif type(sensor) == bytes is True:
    #     print('bytes')
    #     data = sensor

    data = sensor

    addr = writer.get_extra_info('peername')

    #print(f'Received {message!r} from {addr!r}')
    print('Received', message, 'from',addr)

    print('Send: ' , message)
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()

async def main():
   # server = await asyncio.start_server(
    #    handle_echo, '127.0.0.1', 8888)

   server = await asyncio.start_server(
       handle_echo, '192.168.1.39', 8888)


   addr = server.sockets[0].getsockname()
   print('Serving on ', addr)
   logging.info('Server started')

   async with server:
        await server.serve_forever()

asyncio.run(main())