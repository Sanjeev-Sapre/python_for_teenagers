import turtle
scr = turtle.getscreen()
t = turtle.Turtle()

turtle.colormode(255)
t.penup()
x = -200
y = 200
f = 400
while ( x < -30 ):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor( (x+300, y, f-150))
    for i in range(4):
        t.forward(f)
        t.right(90)
    x = x + 10
    y= y- 10
    f = f-20
    t.end_fill()
