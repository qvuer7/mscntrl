import socket
import threading

# Define the server's private IP and port
private_server_ip = '172.31.45.231'
server_port = 2500

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind((private_server_ip, server_port))

# Listen for incoming connections
server_socket.listen(5)  # Allow up to 5 simultaneous connections

print(f"Server is listening on {private_server_ip}:{server_port}")

# List to store connected client sockets
connected_clients = []

# Function to handle each client
def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data_from_client = client_socket.recv(1024).decode()

            if not data_from_client:
                print("Client closed the connection.")
                break


            # Forward the message to other connected clients
            for client in connected_clients:
                if client != client_socket:
                    client.send(data_from_client.encode())

        except KeyboardInterrupt:
            print("Server terminated by user.")
            break

    # Remove the client socket from the list
    connected_clients.remove(client_socket)
    client_socket.close()

# Main server loop
while True:
    try:
        # Accept incoming connections
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Add the client socket to the list
        connected_clients.append(client_socket)

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

    except KeyboardInterrupt:
        print("Server terminated by user.")
        break

# Close the server socket when done
server_socket.close()
