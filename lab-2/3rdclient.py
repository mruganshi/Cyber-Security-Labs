import socket
SERVER = "127.0.0.1"
PORT = 2005
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER, PORT))
while True:
	inp = input("Enter the operation in the form opreand operator oprenad: ")
	if inp == "End":
		break
	client.send(inp.encode())
	answer = client.recv(1024)
	#print("Answer is "+answer.decode())
client.close()
