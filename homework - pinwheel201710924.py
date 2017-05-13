import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
oldPos = t1.pos()
def giyuk(size):
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)
    t1.penup()
    t1.goto(oldPos)
    t1.rt(45)
    t1.pendown()
for i in range(8):
    print(giyuk(100))
wn.exitonclick()
