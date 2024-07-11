import paramiko

def create_ssh(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, port, username=username, password=password)
        print("SSH connection established successfully.")
        return ssh
    except paramiko.AuthenticationException:
        print('Authentication Failed.')
    except paramiko.SSHException as e:
        print(f'An error occurred: {str(e)}')

def main():
    hostname = "192.168.100.5"
    port = 22
    username = "user"
    password = "1234"

    ssh = create_ssh(hostname, port, username, password)
    if ssh is not None:
        ...

if __name__ == "__main__":
    main()