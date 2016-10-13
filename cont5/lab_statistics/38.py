import numpy as np
import matplotlib.pyplot as plt
input = open('img.txt', 'r')
data = [list(map(float, input.readline().split())) for i in range(200)]
flat_data = np.array(data).flatten()
new_data = flat_data.reshape((200, 267))
plt.hist(flat_data, bins=20)
plt.show()