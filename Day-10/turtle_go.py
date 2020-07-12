import turtle

t= turtle.Turtle()
scr = turtle.getscreen()

t.penup()
t.goto( -200, -200)
t.pendown()
t.goto( -200, 200)
t.home()
scr.exitonclick()