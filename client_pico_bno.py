import socket

def open_port():
    #picoIP = '192.168.1.23'
    #picoIP = '10.0.253.239'
    picoIP = '192.168.4.1'

    # Prot must be the same as on the PICO server/
    # TODO make the socket e.g. 35492 a paamenter that can be store in secrets of other config. value is needed in client
    picoPort = 35492

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.connect((picoIP, picoPort))
    #print('client socket established')
    return s

def receive(s):
    try:
        payload = s.recv(100).decode()
        payload = payload.replace('(','').replace(')', '')
        payload = payload.split(',')
        data =[]
        for datum in payload:
            data.append(float(datum))

    except Exception as e:
        print(e)
        s.close()

    return data

def main():
    #print(receive(open_port()))
    return receive(open_port())

if __name__ == '__main__':
    print(main())