import wave

pcmf = open("maria.pcm", 'rb')
pcmdata = pcmf.read()
pcmf.close()

print(pcmdata.__len__())

wavfile = wave.open("output.wav", 'wb')
wavfile.setnchannels(1)
wavfile.setsampwidth(16//8)
wavfile.setframerate(16000)
wavfile.writeframes(pcmdata)
wavfile.close()