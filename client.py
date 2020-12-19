import asyncio
import logging
import configparser
import ast
import pprint


logging.basicConfig(format='%(asctime)s %(lineno)d %(message)s',
                    filename='client.log',
                    level=logging.DEBUG)

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')


async def tcp_echo_client(message):

    ip_addr = config['ADDRESS']['ip_addr']
    reader, writer = await asyncio.open_connection( ip_addr, 8888)
    logging.debug('create reader and writer')

    #print(f'Send: {message!r}')
    writer.write(message.encode())
    logging.info('writer : {}'.format(message))

    n = int(config['DATA']['bytes_length'])  # number of bytes to read


    data = await reader.read(n)
    logging.debug(data.decode)
    logging.debug(data)

    try:
        data_dict = ast.literal_eval(data.decode())  # extract the dictionary from the string received
 #       data_dict = ast.literal_eval(data)  # extract the dictionary from the string received

        logging.debug(data_dict)

    except Exception as e:
        logging.debug(e)

        data_dict = {}

    finally:
        print('Close the connection')
        writer.close()
        logging.info('Close the connection')

    return data_dict


def main():
    received  = asyncio.run(tcp_echo_client('Hello World!'))
    pprint.pprint(received)
    return received

if __name__ == '__main__':
    main()