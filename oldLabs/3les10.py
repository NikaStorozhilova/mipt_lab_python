import turtle
turtle.shape('turtle')
n=2000
a = 10
b=10
for i in range(0, n, 1):
    turtle.penup()
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(b)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(50+(i)*2*b)
    turtle.left(90)
    turtle.forward(50+(i)*2*b)
    turtle.left(90)
    turtle.forward(50+2*(i)*b)
    turtle.left(90)
    turtle.forward(50+2*(i)*b)
    b +=1






