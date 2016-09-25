import turtle
import math
def draw(r):
    n=100
    a=math.sin(math.pi/n)*2*r
    f =360/n
    for i in range(n):
        turtle.forward(a)
        turtle.left(f)
    return(0)
turtle.shape('turtle')
n = 10
turtle.speed(1000)
f = 360/n
for i in range(n):
    draw(50)
    turtle.right(f)