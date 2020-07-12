import turtle
import random
# get a screen
scr = turtle.getscreen()
# Colors are available here https://en.wikipedia.org/wiki/Web_colors
scr.bgcolor('brown')
scr.title( 'Sanjeev Turtle Program')
# get a turtle
t = turtle.Turtle()

t.pencolor("purple")
t.fillcolor("orange")
t.pensize(4)
t.speed(9)
t.begin_fill()
t.circle(90)
t.end_fill()
t.circle(190)






scr.exitonclick()
