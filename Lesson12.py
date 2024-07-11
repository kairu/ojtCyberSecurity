import socket

from Lesson11nettypes import EthernetFrame
from Lesson7 import PCAPFile

class TCPServer:
    def __init__(self):
        ...
    
    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 80))
        server_socket.listen(1)
        print('Server is listening on port 80...')

        connection, address = server_socket.accept()
        print(f'Accepted connection from {address}')

        pcap = PCAPFile('remote.pcap')

        try:
            while True:
                data = connection.recv(1024)
                if not data:
                    break

                pcap.write_packet(data)
                ethernet_frame = EthernetFrame(data)
                print(ethernet_frame)
        except KeyboardInterrupt:
            ...
        finally:
            pcap.close()
            connection.close()
            server_socket.close()
            print('Server closed.')

if __name__ == '__main__':
    server = TCPServer()
    server.start()