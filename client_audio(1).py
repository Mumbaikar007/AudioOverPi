import socket
import pyaudio
import wave



HOST = '192.168.43.173'
PORT = 9876
ADDR = (HOST,PORT)
path= "/home/pi/output.wav"




CHUNK =  4000
FORMAT = pyaudio .paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 0.5
#WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer = CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(path, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()



with open(path, 'rb') as f:
  contents = f.read()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(contents)

client.close()
