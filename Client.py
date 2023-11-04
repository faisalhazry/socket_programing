import socket

def client_program():
    'host = socket.gethostname()  # as both code is running on the same PC'
    host = '127.0.0.1'
    port = 5000  # socket server port number

    # create TCP Socket
    client_socket = socket.socket()

    # connect to the server
    client_socket.connect((host, port))

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from the server: ' + data)  # show in the terminal

        message = input(" -> ")  # again take input

    # close the connection
    client_socket.close()

if __name__ == '__main__':
    client_program()
