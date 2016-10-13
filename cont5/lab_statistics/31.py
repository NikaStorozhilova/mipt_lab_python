import numpy as np

def get_percentile(values, bucket_number):
	return [np.percentile(values, 100 / bucket_number * i) for i in range(bucket_number )]
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
A =get_percentile(values, 5)
A[0] =0.0
print(A)
