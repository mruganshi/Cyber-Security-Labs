import socket
SERVER_ADDRESS = "localhost"
SERVER_PORT = 1234
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
client_socket.sendall(b"Requesting a handshake")
data = client_socket.recv(1024)
print("Received: ", data.decode())
client_socket.close()