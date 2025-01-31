import socket
from struct import unpack
from macaddr import MacAddress

class EthernetFrame:
    length = 14
    def __init__(self, data):
        unpacked_data = unpack('!6s6sH', data[0:self.length])
        self.protocol = socket.ntohs(unpacked_data[2])
        self.destination = MacAddress(data[0:6])
        self.source = MacAddress(data[6:12])
        self.leftover_data = data[self.length:]

    def __str__(self):
        return '''
            Source:         {source}
            Destination:    {destination}
            Protocol:       {protocol}
        '''.format(**self.__dict__)
    
class IPHeader:
    length = 20
    def __init__(self, data):
        unpacked_data = unpack('!BBHHHBBH4s4s', data[0: self.length])
        self.version = data[0] >> 4
        self.header_length = (data[0] & 15) * 4
        self.ttl = unpacked_data[5]
        self.protocol = unpacked_data[6]
        self.source_addr = socket.inet_ntoa(unpacked_data[8])
        self.dest_addr = socket.inet_ntoa(unpacked_data[9])
        self.leftover_data = data[self.length]