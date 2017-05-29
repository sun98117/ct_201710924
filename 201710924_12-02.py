import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
width = wn.window_width()
w3 = (width-40) /3
x1 = 0.0-w3
x2 = 0.0
x3 = 0.0+w3

def drawTriangleAt(x,y,size):
    t1.penup()
    t1.setheading(0)
    t1.goto(x,y)
    t1.pendown()
    t1.write(t1.pos())
    t1.rt(60)
    t1.fd(size)
    for i in range(0,2):
        t1.rt(120)
        t1.fd(size)


def drawSquareAt(x,y,size):
    t1.penup()
    t1.setheading(0)
    t1.goto(x,y)
    t1.pendown()
    t1.write(t1.pos())
    for i in range(0, 4):
        t1.fd(size)
        t1.rt(90)

def drawStarAt(x,y,size):
    t1.penup()
    t1.setheading(0)
    t1.goto(x,y)
    t1.pendown()
    t1.rt(36)
    t1.fd(size)
    for i in range(0,4):
        t1.rt(144)
        t1.fd(size)


drawSquareAt(x1,100,100)
drawTriangleAt(x2,100,100)
drawStarAt(x3,100,100)

wn.exitonclick()
