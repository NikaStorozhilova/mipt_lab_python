import numpy as np
import random as r
import matplotlib.pyplot as plt
r.seed(0)
def get_percentile(values, bucket_number):
	return [np.percentile(values, 100 / bucket_number * i) for i in range(bucket_number )]
def get_percentile_number(value, percentiles):
	for i in range(len(percentiles)):
		if percentiles[i] > value:
			return i -1
	return i
def value_equalization(value, percentiles, add_random = False):
    idx = get_percentile_number(value, percentiles)
    step = 1 / len(percentiles)
    random_noise = r.uniform(idx*step, (idx+1)*step)
    if(add_random):
        new_value = random_noise
    else:
        new_value = idx * step
    return new_value
def values_equalization(values, percentiles, add_random=False):
    return [value_equalization(values[i], percentiles, add_random = add_random) for i in range(len(values))]
input = open('img.txt', 'r')
data = [list(map(float, input.readline().split())) for i in range(200)]
flat_data = np.array(data).flatten()
new_data = flat_data.reshape((200, 267))
values = flat_data
percentiles =get_percentile(values, 30)
percentiles[0] =0.0
flat_data2 = values_equalization(values, percentiles, add_random=True)
new_data2 = np.array(flat_data2).reshape((200, 267))

plt.subplot(2,2, 1)
plt.imshow(data, cmap = plt.get_cmap('gray'))

plt.subplot(2,2, 2)
plt.hist(flat_data, bins=20)

plt.subplot(2,2, 3)
plt.imshow(new_data2, cmap = plt.get_cmap('gray'))

plt.subplot(2,2, 4)
plt.hist(flat_data2, bins=20)
plt.show()