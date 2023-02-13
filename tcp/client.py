import socket
import sys
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = './tcp_socket_file'

print('Connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as e:
    print(e)
    sys.exit(1)

try:
    fake = Faker()
    message = fake.text()
    sock.sendall(message.encode())
    sock.settimeout(2)
    try:
        while True:
            data = str(sock.recv(32))
            if data:
                print('Received: ' + data)
            else:
                break
    except (TimeoutError):
        print('Socket timeout, ending listening for server messages.')
finally:
    print('Closing socket')
    sock.close()
