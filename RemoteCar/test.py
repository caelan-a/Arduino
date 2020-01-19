import threading
import queue
import time

threads = []

q = queue.Queue()

def recorder():
	print("Recording")
	for i in range(0,10):
		if(q.empty() == False):
			stop_recording_signal = q.get()
			print("Signal: {}".format(stop_recording_signal))
			q.task_done()
			break

		print(i)
		time.sleep(1)
	print("Finished thread")


t = threading.Thread(target=recorder)
t.start()
threads.append(t)

time.sleep(3)
print("Stopping recorder")
q.put("stop")
t.join()
q.join()       # block until all tasks are done
