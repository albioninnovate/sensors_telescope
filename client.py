import asyncio
import logging
import configparser
import ast

logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='client.log',
                    level=logging.DEBUG)

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')


async def tcp_echo_client(message):

    reader, writer = await asyncio.open_connection('192.168.1.39', 8888)
    logging.debug('create reader and writer')

    #print(f'Send: {message!r}')
    writer.write(message.encode())
    logging.info('writer : {}'.format(message))

    n = int(config['DATA']['bytes_length'])

    #n = 500
    data = await reader.read(n)
    #print(f'Received: {data.decode()!r}')
    logging.debug(data.decode)

    try:
        data_dict = ast.literal_eval(data.decode())  # extract the dictionary from the string received
        logging.debug(data_dict)

    except Exception as e:
        logging.debug(e)
        print('Some values returned Null, not able to extract data')
        print('--')
        data_dict = {}
        pass

    finally:
        print('Close the connection')
        writer.close()
        logging.info('Close the connection')

    return data_dict


def main():
    received  = asyncio.run(tcp_echo_client('Hello World!'))
    return received

if __name__ == '__main__':
    main()