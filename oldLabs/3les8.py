import turtle
turtle.shape('turtle')
n=2000
for i in range(1, n, 1):
    turtle.left(3.6)
    turtle.forward(4+ i//100)
    i += 1


input()