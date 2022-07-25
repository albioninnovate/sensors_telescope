import socket
import time

def open_port():
    picoIP = '192.168.1.23'
    #picoIP = '10.0.254.252'

    picoPort = 35492

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    s.connect((picoIP, picoPort))
    #print('client socket established')
    return s

#msg = b'hello'

#while True:
#s.sendall(msg)
#print('sent :',msg)

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