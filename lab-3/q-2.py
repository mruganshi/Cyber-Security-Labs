import socket
HOST = 'localhost'
PORT = 80

b = 6

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Waiting for client on port {PORT}...")
client_socket, address = server_socket.accept()
print(f"Just connected to {address}")

print(f"From Server : Private Key = {b}")
data = client_socket.recv(1024).decode()
clientP = int(data) 

print(f"From Client : P = {clientP}")
data = client_socket.recv(1024).decode()
clientG = int(data) 

print(f"From Client : G = {clientG}")
data = client_socket.recv(1024).decode()
clientA = int(data) 

print(f"From Client : Public Key = {clientA}")
B = pow(clientG, b, clientP) 
Bstr = str(B)

client_socket.sendall(Bstr.encode()) 
Bdash = pow(clientA, b, clientP) 
print(f"Secret Key to perform Symmetric Encryption = {Bdash}")
client_socket.close()
