import socket
from Lesson11nettypes import EthernetFrame
from Lesson7 import PCAPFile

def main():
    sniffing_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    forwarding_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    forwarding_socket.connect(('localhost', 8080))
    pcap = PCAPFile('remotexa.pcap')

    while True:
        data, addr = sniffing_socket.recvfrom(65535)
        
        if len(data) > EthernetFrame.length:
            ethernet_frame = EthernetFrame(data)
            print(ethernet_frame)
            forwarding_socket.sendall(data)
            pcap.write(data)

if __name__ == '__main__':
    main()