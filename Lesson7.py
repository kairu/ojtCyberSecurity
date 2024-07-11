import struct
import time
import socket

class PCAPFile:
    def __init__(self, filename):
        self.pcap_file = open(filename, 'wb')
        self.write_global_header()

    def write_global_header(self):
        global_header = struct.pack('IHHiIII',
                                    0xa1b2c3d4,  # magic number
                                    2,            # major version number
                                    4,            # minor version number
                                    0,            # GMT to local correction
                                    0,            # accuracy of timestamps
                                    65535,        # max length of captured packets
                                    1)            # data link type (Ethernet)
        self.pcap_file.write(global_header)

    def write_packet(self, data):
        ts_sec, ts_usec = map(int, str(time.time()).split('.'))
        length = len(data)
        packet_header = struct.pack('IIII', ts_sec, ts_usec, length, length)
        self.pcap_file.write(packet_header)
        self.pcap_file.write(data)

    def close(self):
        self.pcap_file.close()

def main():
    pcap = PCAPFile('packets.pcap')
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        data, _ = sock.recvfrom(65535)
        pcap.write_packet(data)

if __name__ == "__main__":
    main()
