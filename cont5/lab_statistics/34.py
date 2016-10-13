import numpy as np
import random as r
def get_percentile(values, bucket_number):
	return [np.percentile(values, 100 / bucket_number * i) for i in range(bucket_number )]
def get_percentile_number(value, percentiles):
	for i in range(len(percentiles) - 1):
		if percentiles[i] > value:
			return i - 1
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
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
value = 5.5
percentiles =get_percentile(values, 5)
percentiles[0] =0.0
print(value_equalization(value, percentiles, add_random=True))