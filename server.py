import asyncio
import bno055
import logging
import configparser


logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='server.log',
                    level=logging.DEBUG)

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')


async def handle_echo(reader, writer):
    n = 500
    data = await reader.read(n)
    message = data.decode()

    sensor = bno055.main(output_format='json')
    logging.info('Read sensor')
    print('sensor', sensor)

    data = sensor

    addr = writer.get_extra_info('peername')
    logging.info(addr)	

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
