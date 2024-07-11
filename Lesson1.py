import socket

class CreateHost:
      def __init__(self):
          ...

      def add_attribute(self, name, value):
         setattr(self, name, value)

      def remove_attr(self, name):
           if hasattr(self, name):
                delattr(self, name)

      def socket_close(self):
           if hasattr(self, 'socket'):
            self.socket.close()

      def is_open(self, timeout):
         try:
              with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                  sock.settimeout(timeout)
                  result = sock.connect_ex((self.host, self.port))
                  if result:
                      raise socket.error(f'Connection failed. Error code: {result}')
                  print('Connection established successfully')
         except socket.error as e:
               print(f'An error occured: {str(e)}')

def main():
   # Create Class
   host = CreateHost()
   host.add_attribute('host','192.168.100.5')
   host.add_attribute('port', 5000) #3306 for successful
   host.is_open(800) # var timeout in ms

if __name__ == '__main__':
	main()