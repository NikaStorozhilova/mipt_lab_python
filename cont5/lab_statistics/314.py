import numpy as np
import random as r
import matplotlib.pyplot as plt
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
A = r.sample(data, 100)
flat_A = np.array(A).flatten()
values = flat_A
percentiles =get_percentile(values, 30)
percentiles[0] =0.0
flat_A2 = values_equalization(values, percentiles, add_random=True)
new_A = np.array(flat_A).reshape((100, 267))
print(sum(flat_A2)/len(flat_A2))
plt.imshow(new_A, cmap = plt.get_cmap('gray'))
plt.show()