import socket

class Grabber:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.ip, self.port))
            self.socket.settimeout(1000 / 1000.0) # timeout in ms
        except socket.error as e:
            print(f'Error connecting to {self.ip}: {self.port} - {e}')

    def read(self, length=1024):
        try:
            return self.socket.recv(length)
        except Exception as e:
            print(f'Error: {e}')
            return b"Error occurred"
    
    def close(self):
        self.socket.close()
    
def main():
    ip = '192.168.100.5'
    ports_to_scan = range(4985, 5010)

    for port in ports_to_scan:
        grabber = Grabber(ip, port)
        banner = grabber.read()
        grabber.close()

        print(f'Port {port}: {banner.decode(errors="ignore").strip()}')

if __name__ == "__main__":
    main()