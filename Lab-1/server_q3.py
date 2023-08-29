import socket
SERVER_ADDRESS = "localhost"
SERVER_PORT = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen()
print("Listening for incoming connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Connection from", client_address, "has been established.")
    data = client_socket.recv(1024)
    client_socket.sendall(data)
    client_socket.close()
server_socket.close()