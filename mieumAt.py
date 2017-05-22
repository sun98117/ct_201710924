import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def giyukAt(size,x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)

def nieunAt(size,x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.rt(90)
    t1.fd(100)
    t1.lt(90)
    t1.fd(100)

def mieumAt(size,x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    giyukAt(size,x,y)
    t1.lt(90)
    nieunAt(size,x,y)
mieumAt(100,-100,100)

wn.exitonclick()