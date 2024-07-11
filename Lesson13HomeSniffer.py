import socket
from Lesson11nettypes import EthernetFrame
from Lesson7 import PCAPFile

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    print('Server now listening on port 8080...')

    while True:
        conn, addr = server.accept()
        print(f'Accepted connection from {addr}')

        while True:
            data = conn.recv(1024)
            if data:
                ethernet_frame = EthernetFrame(data)
                print(ethernet_frame)
                print(data)
            else:
                break

        conn.close()
        print('Connection closed.')

if __name__ == '__main__':
    main()