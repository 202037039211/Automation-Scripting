import socket

def receive_file(conn, fileno):
    """
    Receives a file from the client and saves it with a new name.
    """
    data = conn.recv(1024).decode()
    if not data:
        return

    filename = f'output{fileno}.txt'
    with open(filename, 'w') as fo:
        while data:
            fo.write(data)
            data = conn.recv(1024).decode()

    print(f"Received file successfully! Saved as {filename}")

if __name__ == "__main__":
    # Define the socket parameters
    host = ""  # Server's IP address or hostname
    port = 8080  # Port for communication
    total_clients = int(input("Enter the number of clients: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(total_clients)
    connections = []

    print('Waiting for clients to connect...')

    # Accept connections from clients
    for i in range(total_clients):
        conn, addr = sock.accept()
        connections.append(conn)
        print(f'Client {i + 1} connected from {addr}')

    # File receiving loop
    fileno = 0
    for conn in connections:
        fileno += 1
        print(f'Receiving file from client {fileno}...')
        receive_file(conn, fileno)

    # Close all connections
    for conn in connections:
        conn.close()
