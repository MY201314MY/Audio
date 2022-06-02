import wave
import struct

pcmf = open("ring.pcm", 'rb')
pcmdata = pcmf.read()
pcmf.close()

print("PCM len", pcmdata.__len__())
print(type(pcmdata))

wavfile = wave.open("ring.wav", 'wb')
wavfile.setnchannels(1)
wavfile.setsampwidth(16//8)
wavfile.setframerate(8000)
wavfile.writeframes(pcmdata)
wavfile.close()