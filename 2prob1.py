import math


def f(x):
    return math.log((math.exp(1/(math.sin(x)+1))/(5/4+1/x**15)), 1+x**2)
print (f(1))
print (f(10))
print (f(1000))