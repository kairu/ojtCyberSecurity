from Lesson11nettypes import EthernetFrame, UDPSegment
from Lesson9 import IPHeader
from Lesson10 import TCPSegment
import socket

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(65535)
        eth_frame = EthernetFrame(raw_data)
        print(eth_frame)
        if eth_frame.protocol == 8:
            ipheader = IPHeader(eth_frame.leftover_data)
            print(ipheader)
            if ipheader.protocol == 6:
                tcp = TCPSegment(ipheader.leftover_data)
                print(tcp)
            elif ipheader.protocol == 17:
                udp = UDPSegment(ipheader.leftover_data)
                print(udp)

if __name__ == "__main__":
    main()