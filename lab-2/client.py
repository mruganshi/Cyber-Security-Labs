import socket
SERVER = "localhost"
PORT = 2005
client2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client2.connect((SERVER, PORT))
while True:	
	inp2 = input("Enter the operation in the form opreand operator oprenad: ")
	if inp2 == "End":
		break
	client2.send(inp2.encode())
	answer = client2.recv(1024)
	print("Answer is "+answer.decode())
client2.close()
