import socket               
 
sock = socket.socket()
 
host = "192.168.1.84" #ESP32 IP in local network
port = 80             #ESP32 Server Port    
 
sock.connect((host, port))
 
from inputs import devices, get_gamepad
import serial, time

MAX_ANALOG_OFFSET = 31687

POWER_PREFIX = 'p'
TURN_PREFIX = 't'

print("Welcome to PiCar")

def sendData(data, prefix):
	data_enc = ('<' + prefix + str(data) + '>').encode();
	print(data_enc)
	sock.send(data_enc)


def getNormalised(num):
	normalised = event.state / MAX_ANALOG_OFFSET
	if(normalised > 1):
		normalised = 1.0
	elif(normalised < -1):
		normalised = -1.0
	normalised = round(normalised, 2)
	return normalised


def checkThumbSticks(event):
	if(event.code == 'ABS_Y'):
		sendData(getNormalised(event.state), TURN_PREFIX)
	# elif(event.code == 'ABS_RX'):
	# 	sendData(getNormalised(event.state), TURN_PREFIX)


while True:
	events = get_gamepad()
	for event in events:
		checkThumbSticks(event)
