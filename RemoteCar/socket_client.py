import socket               
 
sock = socket.socket()
 
host = "192.168.1.84" #ESP32 IP in local network
port = 80             #ESP32 Server Port    
 
sock.connect((host, port))
 
message = b"1"
sock.send(message)
 
# data = ""       
 
# while len(data) < len(message):
#     data += sock.recv(1)
 
# print(data)
 
# sock.close()
