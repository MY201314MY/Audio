import numpy as np
import struct

time = np.zeros(shape=5760, dtype=np.int16)
value = np.zeros(shape=5760, dtype=np.int16)
with open(file="output.txt", mode="r") as f:
    x = f.readlines()

for i in range(5760):
    time[i] = i

for item in x:
    value[int(item[2:6])] = int(item[13:-1])
with open(file="maria.pcm", mode="wb+") as pcm:
    for i in range(5760):
        pcm.write(struct.pack("h", value[i]))
        #print("i:{0} -- value:{1}".format(i, value[i]))
