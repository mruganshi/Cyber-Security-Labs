import socket
import sys

def evaluate_expression(expression):
    return eval(expression)

def communicate_with_server(server_address, server_port):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server
    client_socket.connect((server_address, server_port))

    while True:
        # Ask the user for input
        expression = input("Enter an expression: ")

        # Send the expression to the server
        client_socket.sendall(expression.encode('utf-8'))

        # Receive the result from the server
        result = client_socket.recv(1024).decode('utf-8')

        # Display the result
        print(f"Result: {result}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python client.py [server address] [server port]")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])

    communicate_with_server(server_address, server_port)
