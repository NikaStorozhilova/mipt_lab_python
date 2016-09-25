import turtle
import math
def draw(n, a):
    f = 180 - 180 * (n - 2) / n
    for i in range(n):
        turtle.forward(a)
        turtle.left(f)
    return(0)
turtle.shape('turtle')
a = 100
r = a/math.sin(180/3)/2
