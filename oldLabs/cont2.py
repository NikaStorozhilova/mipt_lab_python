c = 0
k = 0
t = 0
a = int(input())
while a !=0:
    c += a
    t += a**2
    k += 1
    a = int(input())
j = c / k
n = t / k
m = ((n - j ** 2) * k / (k - 1)) ** (0.5)
print(m)