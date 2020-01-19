import serial, time
arduino = serial.Serial('COM9', 115200, timeout=.1)
time.sleep(1)
arduino.write("Hello from Python!")
while True:
	data = arduino.readline()
	if data:
		print data.rstrip('\n') #strip out the new lines for now
		# (better to do .read() in the long run for this reason