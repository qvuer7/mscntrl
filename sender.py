import socket
import pyautogui as pg

public_server_ip = '54.198.62.240'
server_port = 2500


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((public_server_ip, server_port))

while True:
    try:

        x, y = pg.position()
        message_to_server = f'{x} {y}'
        client_socket.send(message_to_server.encode())

        # Receive data from the server
        data_from_server = client_socket.recv(1024).decode()

        if not data_from_server:
            print("Server closed the connection.")
            break

        print("Received from server:", data_from_server)

    except KeyboardInterrupt:
        print("Client terminated by user.")
        break

# Close the client socket when done
client_socket.close()
