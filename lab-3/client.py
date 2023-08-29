import socket
HOST = 'localhost'
PORT = 80

p = 11
g = 7
a = 3

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connecting to ", HOST, " on port ", PORT)

    s.sendall(str(p).encode())
    print("Sent p = ", p)

    s.sendall(str(g).encode())
    print("Sent g = ", g)

    A = (g ** a) % p
    s.sendall(str(A).encode())
    print("Sent public key A = ", A)

    B = s.recv(1024)
    print("Received public key B = ", B.decode())

    B = float(B.decode())
    Adash = (B ** a) % p
    print("Secret key to perform Symmetric Encryption = ", Adash)
