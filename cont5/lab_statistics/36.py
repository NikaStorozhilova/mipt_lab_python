input = open('img.txt', 'r')
data = [list(map(float, input.readline().split())) for i in range(200)]
