import socket
SERVER_ADDRESS = "iitj.ac.in"
SERVER_PORT = 80
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
client_socket.sendall(b"Hello, server!")
data = client_socket.recv(1024)
print("Received: ", data.decode())
client_socket.close()