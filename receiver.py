import socket
import threading


public_server_ip = '54.198.62.240'
server_port = 2500

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((public_server_ip, server_port))

def listen_for_messages():
    while True:
        try:

            data_from_server = client_socket.recv(1024).decode()
            print(data_from_server)

        except KeyboardInterrupt:
            break

listener_thread = threading.Thread(target=listen_for_messages)
listener_thread.start()


