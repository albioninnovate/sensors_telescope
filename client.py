import asyncio
import logging
import configparser
import ast
import pprint
import time

def start_logging():
    logging.basicConfig(format='%(asctime)s %(lineno)d %(message)s',
                        filename='client.log',
                        level=logging.INFO)

def stat_config():
    # Read config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

#TODO put the configparseer in a method so that it is avaiable when called as a module

async def tcp_echo_client(message):

    #ip_addr = config['ADDRESS']['ip_addr']
    reader, writer = await asyncio.open_connection( '192.168.1.21', 8888)
    logging.debug('create reader and writer')

    #print(f'Send: {message!r}')
    writer.write(message.encode())
    logging.info('writer : {}'.format(message))

    #n = int(config['DATA']['bytes_length'])  # number of bytes to read
    time.sleep(1)  # allow time for the data to be received
    data = await reader.read(500000)
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
        writer.close()
        logging.info('Close the connection')
        #print(data_dict)
    return data_dict


def main():
    start_logging()
    stat_config()
    received  = asyncio.run(tcp_echo_client('data pls, Thk you'))
    #print('received by client')
    #pprint.pprint(received)
    return received

if __name__ == '__main__':
    main()