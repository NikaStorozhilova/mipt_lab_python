import numpy as np
import random as r
import matplotlib.pyplot as plt
input = open('img.txt', 'r')
data = [list(map(float, input.readline().split())) for i in range(200)]
A = [r.choice(data) for i in range(100)]
plt.imshow(A, cmap = plt.get_cmap('gray'))
plt.show()