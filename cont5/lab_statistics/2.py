import random as r

def function(x):
	if x <= 2 and x >= -2:
		return -x ** 2 + 4
	else:
		return 0
n = 10000000
a = -3
b = 3
val = [function(r.uniform(a, b)) for i in range(n)]
answer = (b - a) / n * sum(val)
print(answer)