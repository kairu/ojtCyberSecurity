import socket

def main():
    raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = raw_socket.recvfrom(65535)
        print(raw_data)

if __name__ == "__main__":
    main()