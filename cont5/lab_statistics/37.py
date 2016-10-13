import matplotlib.pyplot as plt
input = open('img.txt', 'r')
data = [list(map(float, input.readline().split())) for i in range(200)]
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.show()