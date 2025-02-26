from socket import *
import sys

server_IP = "localhost"
server_port = 8000

# Validate user input
while True:
    try:
        client_number = int(input("Enter an integer between 1 and 100: "))
        if 1 <= client_number <= 100:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Create client socket
client_socket = socket(AF_INET, SOCK_STREAM)
print("Client: Attempting to connect to server...")
client_socket.connect((server_IP, server_port))
print("Client: Connected to server.")

# Construct message with client name and number
client_name = "Client: Zachery"  
message = f"{client_name},{client_number}"

# Send message to server
print(f"Client: Sending message to server: {message}")
client_socket.send(message.encode())

# Receive message from server
server_response = client_socket.recv(2048).decode()
print(f"Client: Received response from server: {server_response}")

# Parse server response
server_name, server_number = server_response.split(',')
server_number = int(server_number)

# Display results
print(f"{client_name}\n{server_name}\nClient number: {client_number}\nServer number: {server_number}\nSum: {client_number + server_number}")

# Close the socket
client_socket.close()
print("Client: Connection closed.")
