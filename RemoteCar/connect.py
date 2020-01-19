# import socket
# IP1 = socket.gethostbyname(socket.gethostname()) # local IP adress of your computer
# print(IP1)
IP2 = socket.gethostbyname('raspberrypi') # IP adress of remote computer
print(IP2)
