import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
width = wn.window_width()
w3 = (width-40) /3
x1 = 0.0-w3
x2 = 0.0
x3 = 0.0+w3

def drawTriangleAt(at,size):
    t1.penup()
    t1.setheading(0)
    t1.goto(at,0)
    t1.pendown()
    t1.write(t1.pos())
    t1.rt(60)
    t1.fd(size)
    t1.rt(120)
    t1.fd(size)
    t1.rt(120)
    t1.fd(size)

def drawPentagonAt(at,size):
    t1.penup()
    t1.setheading(0)
    t1.goto(at,0)
    t1.pendown()
    t1.write(t1.pos())
    t1.rt(108)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)

def drawStarAt(at,size):
    t1.penup()
    t1.setheading(0)
    t1.goto(at,0)
    t1.pendown()
    t1.rt(36)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)

drawTriangleAt(x1,100)
drawPentagonAt(x2,100)
drawStarAt(x3,100)

wn.exitonclick()