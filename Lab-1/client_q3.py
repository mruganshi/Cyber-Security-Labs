import socket
SERVER_ADDRESS = "localhost"
SERVER_PORT = 1234
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
data = input("Enter a message to send to the server: ")
client_socket.sendall(data.encode())
data = client_socket.recv(1024)
print("Received from server:", data.decode())
client_socket.close()