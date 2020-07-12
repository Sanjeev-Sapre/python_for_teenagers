import turtle

scr = turtle.getscreen()
t = turtle.Turtle()


t.penup()
x = -200
y = 200
f = 400
while ( x < -70 ):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.forward(f)
        t.right(90)
    x = x + 10
    y= y- 10
    f = f-20
