import turtle
turtle.shape('turtle')
for i in range(10, 180, 10):
    turtle.left(90)
    turtle.backward(i)
    turtle.left(90)
    turtle.backward(i)


input()