from socket import *
import random

server_IP = "localhost"
server_port = 8000
server_name = "Server: Zachery"  

# Create server socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_IP, server_port))
server_socket.listen(1)

print("The server is ready to receive")

while True:
    # Accept a connection from a client
    connection_socket, addr = server_socket.accept()
    print("Server: Connection established with", addr)
    
    # Receive the message from the client
    client_message = connection_socket.recv(2048).decode()
    client_name, client_number = client_message.split(',')
    client_number = int(client_number)
    
    # Server picks a random number between 1 and 100
    server_number = random.randint(1, 100)
    
    # Display client info and sum
    print(f"{client_name}\n{server_name}\nClient number: {client_number}\nServer number: {server_number}\nSum: {client_number + server_number}")
    
    # Send server response back to client
    response_message = f"{server_name},{server_number}"
    print(f"Server: Sending response to client: {response_message}")
    connection_socket.send(response_message.encode())
    
    # Close connection
    connection_socket.close()
    print("Server: Connection closed.")
