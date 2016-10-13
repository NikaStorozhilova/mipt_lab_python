import random
import matplotlib.pyplot as plt

plt.subplot(2,2, 1)
random.seed(0)
n = 100
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

plt.subplot(2,2, 2)
random.seed(0)
n = 1000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

plt.subplot(2,2, 3)
random.seed(0)
n = 10000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

plt.subplot(2,2, 4)
random.seed(0)
n = 100000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
plt.show()