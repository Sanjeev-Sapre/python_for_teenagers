import turtle
s = turtle.Turtle()


s.color("blue", "red")  # first one is line color and next is fill color

s.begin_fill()
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.end_fill()

s.penup()
s.forward(30)
s.pendown()

s.color("green", "blue")
s.begin_fill()
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.end_fill()

s.penup()
s.forward(130)
s.pendown()

s.color("green", "green")
s.begin_fill()
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.end_fill()

s.penup()
s.forward(130)
s.pendown()

s.color("yellow", "yellow")
s.begin_fill()
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.end_fill()

turtle.done()

