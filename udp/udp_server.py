import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = './udp_socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)

while True:
    print('Receiving message from client side.')
    data, client_address = sock.recvfrom(4096)
    print(data.decode())

    if data:
        print(f'Response: Send {data} back to {client_address}')
        sent = sock.sendto(data, client_address)