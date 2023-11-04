import socket

def Main():

    # Get the hostname
    "host = socket.gethostname()"
    host = '127.0.0.1'
    port = 5000 # initiate port no above 1024

    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Bind the host address and port together
    server_socket.bind((host, port))

    # Listen for incoming connection
    server_socket.listen(2)

    # Accept new connection
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        # receiive data stream. it won't accept packet greater than 1024 bytes
        data = conn.recv(1024).decode() ###  WHY
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode()) # send data to the client

        # close the connection
    conn.close()

if __name__=='__main__':
     Main()
     
     
     
