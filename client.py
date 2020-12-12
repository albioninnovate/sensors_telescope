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

    #n = int(config['DATA']['characters'])

    n = 500
    data = await reader.read(n)
    #print(f'Received: {data.decode()!r}')

    try:
        data_dict = ast.literal_eval(data.decode())  # extract the dictionary from the string received
        #print(data_dict)
        # print('Euler angles : ', data_dict['Euler angle'])

    except:
        print('Some values returned Null, not able to extract data')
        print('--')
        data_dict={'Euler angle' : [0.0,0.0,0.0]}
        pass

    finally:
        print('Close the connection')
        writer.close()

    return data_dict

def main():
    received  = asyncio.run(tcp_echo_client('Hello World!'))
    return received

if __name__ == '__main__':
    main()
