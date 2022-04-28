import matplotlib.pyplot as plt
import numpy as np

time = np.zeros(shape=5760, dtype=np.int16)
value = np.zeros(shape=5760, dtype=np.int16)
with open(file="output.txt", mode="r") as f:
    x = f.readlines()

for i in range(5760):
    time[i] = i

for item in x:
    value[int(item[2:6])] = int(item[13:-1])
    print("{0} -- {1}".format(item[2:6], item[13:-1]))

plt.figure(figsize=(16, 9))
plt.plot(time, value)
plt.show()