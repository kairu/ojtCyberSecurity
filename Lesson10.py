from struct import unpack
class TCPSegment:
    length = 20
    def __init__(self, data):
        unpacked_data = unpack('!HHLLBBHHH', data[0:self.length])
        self.src_port = unpacked_data[0]
        self.dest_port = unpacked_data[1]
        self.sequence = unpacked_data[2]
        self.acknowledgement = unpacked_data[3]
        self.doffset_reserved = unpacked_data[4]
        self.header_length = self.doffset_reserved >> 4
        self.leftover_data = self.parse_http_data(data[self.length:])

    def __str__(self):
        return '''
            TCPSegment:
            - Source Port:          {src_port}
            - Destination Port:     {dest_port}
            - Data:                 {leftover_data}
        '''.format(**self.__dict__)
    
    def _parse_http_data(self, data):
        try:
            return data.decode('utf-8')
        except Exception as e:
            return data