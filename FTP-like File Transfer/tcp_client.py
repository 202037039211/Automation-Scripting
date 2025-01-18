import socket

def send_file(filename, sock):
    """
    Sends a file to the connected server.
    """
    try:
        with open(filename, 'r') as fi:
            data = fi.read()
            if not data:
                print("The file is empty.")
                return

            while data:
                sock.send(str(data).encode())
                data = fi.read()
    except IOError:
        print("Invalid filename. Please try again.")

if __name__ == "__main__":
    # Define the socket parameters
    host = ""  # Server's IP address or hostname
    port = 8080  # Port for communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host, port))
    except ConnectionError:
        print("Connection failed. Check the server and try again.")
        exit()

    # File transfer loop
    while True:
        filename = input('Enter the filename you want to send/transfer: ')
        send_file(filename, sock)

    sock.close()
