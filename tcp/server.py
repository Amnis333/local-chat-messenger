import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = './tcp_socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('Connection from ' , client_address)
        while True:
            data = connection.recv(32)
            data_str = data.decode('utf-8')
            print('Received ' + data_str)
            if data:
                #response = 'Processing ' + data_str
                connection.sendall(data_str.encode())
            else:
                print('no data from', client_address)
                break
    finally:
        print('Closing socket')
        connection.close()
