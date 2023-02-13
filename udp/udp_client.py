import socket
from faker import Faker
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

client_address = './udp_client_socket_file'
server_address = './udp_socket_file'
faker = Faker()
message = faker.text()

try:
    os.unlink(client_address)
except FileNotFoundError:
    pass

sock.bind(client_address)

try:
    print(f'Client send encoded message ({message}) to {server_address}.')
    sent = sock.sendto(message.encode(), server_address)
    data, address = sock.recvfrom(4096)
    print('Now received response from serverside.')
    print(data)
finally:
    print('Closing socket.')
    sock.close()
