import socket
SERVER_ADDRESS = "localhost"
SERVER_PORT = 2005
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen()
print("Server started")
print("Waiting for client request..")
clientConnection, clientAddress = server_socket.accept()
print("Connected client :", clientAddress)
msg = ''
while True:
	data = clientConnection.recv(1024)
	msg = data.decode()
	ans=eval(msg)
	print("Send the result to client")
	output = str(ans)
	clientConnection.send(output.encode())
clientConnection.close()
