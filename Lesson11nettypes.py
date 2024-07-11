import struct, socket
from macaddr import MacAddress

class EthernetFrame:
    def __init__(self, data):
        self.length = 14
        self.source, self.destination, self.protocol, self.leftover_data = self.parse_ethernet_frame(data)

    def parse_ethernet_frame(self, data):
        parsed_data = struct.unpack("!6s6sH", data[:self.length])
        source = self.mac_addr(parsed_data[0])
        destination = self.mac_addr(parsed_data[1])
        protocol = socket.ntohs(parsed_data[2])
        leftover_data = data[self.length]
        return source, destination, protocol, leftover_data
    
    def mac_addr(self, bytestring):
        return ':'.join("{:02x}".format(x) for x in bytestring).upper()
    
    def __str__(self):
        return f'Source: {self.source}, Destination: {self.destination}, Protocol: {self.protocol}'
    
class UDPSegment:
    length = 8
    def __init__(self, data):
        unpacked_data = struct.unpack('!HHHH', data[0:self.length])
        self.src_port = unpacked_data[0]
        self.dest_port = unpacked_data[1]
        self.length = unpacked_data[2]
        self.checksum = unpacked_data[3]
        self.leftover_data = data[self.length:]

    def __str__(self):
        return '''
            UDPSegment:
            - Source Port:          {src_port}
            - Destination Port:     {dest_port}
            - Checksum:             {checksum}
            - Data:                 {leftover_data}
        '''.format(**self.__dict__)
        