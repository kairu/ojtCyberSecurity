import socket, concurrent.futures
class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []
    
    def is_open(self, port, timeout):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout / 1000.0)
                result = sock.connect_ex((self.ip, port))
                return result == 0
        except Exception as e:
            print(f'Error checking port {port}: {e}')
            return False
    
    def scan(self, lowerport, upperport, timer = 5000, max_threads=7):
        with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
            futures = {executor.submit(self.is_open, port, timer): port for port in range(lowerport, upperport + 1)}
            results = concurrent.futures.wait(futures.keys(), timeout=timer / 1000.0)
            # print(', '.join(str(future.done()) for future in futures.keys()))
            for future in results.done:
                if future.result():
                    self.open_ports.append(futures[future])
                    
    
    def write_to_file(self, filepath):
        _newline = '\n'
        with open (filepath,"w") as f:
            f.write(f'{_newline.join(str(port) for port in self.open_ports)}')

def main():
    ip = '192.168.100.5'
    scanner = Scanner(ip)
    lowerport = 4995
    upperport = 5005
    timer = 800# add a timer in ms for faster scanning
    max_threads = 7 # Bugged, using > 6 results in no port scanned.
    scanner.scan(lowerport, upperport, timer, max_threads)

    output_file = 'open_ports.txt'
    scanner.write_to_file(output_file)
    print(f'Open ports: {scanner.open_ports}')

if __name__ == "__main__":
    main()