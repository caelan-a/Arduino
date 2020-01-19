import random
import pyaudio

def group(n, items):
    ns = [iter(items)] * n
    while True:
        yield [next(a) for a in ns]

p = pyaudio.PyAudio()

rate = 44100
stream1 = p.open(format=pyaudio.paInt8, channels=1, rate=rate, output=True)
stream2 = p.open(format=pyaudio.paInt8, channels=1, rate=rate, output=True)

frame_size = 1024
for frame in group(frame_size, range(rate)):
    d1 = bytes(n % 256 for n in frame)
    d2 = bytes(int(random.random() * 256) for _ in frame)
    stream1.write(d1)
    stream2.write(d2)

stream1.stop_stream()
stream2.stop_stream()

stream1.close()
stream2.close()

p.terminate()