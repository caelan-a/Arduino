import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Starting up on {} port {}'.format(server_address[0], server_address[1]))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("Waiting for connection")
    connection, client_address = sock.accept()
    try:
	    print('Connection from {}'.format(client_address))

	    # Receive the data in small chunks and retransmit it
	    while True:
	        data = connection.recv(16)
	        print ('Received "%s"'.format(data))
	        if data:
	            print('Sending data back to the client')
	            connection.sendall(data)
	        else:
	            print ('no more data from {}'.format(client_address))
	            break
	            
    finally:
        # Clean up the connection
        connection.close()