import socket
import re

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        match = re.match(r'(\d+) ([\+\-\*\/]) (\d+)', data)
        if match:
            a, op, b = match.groups()
            a, b = int(a), int(b)
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a / b
            else:
                result = 'Invalid operator'

            client_socket.sendall(str(result).encode('utf-8'))

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)

    while True:
        client_socket, address = server_socket.accept()
        handle_client(client_socket)
        client_socket.close()

if __name__ == '__main__':
    start_server(5555)
