import numpy as np

def get_percentile(values, bucket_number):
	return [np.percentile(values, 100 / bucket_number * i) for i in range(bucket_number )]
def get_percentile_number(value, percentiles):
	for i in range(len(percentiles) - 1):
		if percentiles[i] > value:
			return i - 1
	return i
def value_equalization(value, percentiles):
	idx = get_percentile_number(value, percentiles)
	step = 1 / len(percentiles)
	new_value = idx * step
	return new_value
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
value = 5.5
A =get_percentile(values, 4)
A[0] =0.0
print(value_equalization(5.5, A))