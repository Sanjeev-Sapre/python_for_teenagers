import turtle
import random
# get a screen
scr = turtle.getscreen()
# Colors are available here https://en.wikipedia.org/wiki/Web_colors
# red 0 to 255
# green , blue
scr.colormode(255)
x= -200
y=200



scr.title( 'Sanjeev Turtle Program')
# get a turtle
t = turtle.Turtle()
  # 0 Fastest , 1 to 10 slow to fast -- 1 is slowest, 10 is maximum
t.begin_fill()

def draw_square(side_length):
    t.penup()
    t.goto(random.randint( -200, 300), random.randint( -200, 300))
    t.penup()
    r = random.randint( 0,255)
    g = random.randint( 0,255)
    b = random.randint( 0,255)

    t.speed ( random.randint( 0, 10 ))
    t.pencolor( r,g,b)
    for i in range(4):
        t.forward( side_length)
        t.right(90)


for i in range( 50   ):
    t.begin_fill()
    r = random.randint( 0,255)
    g = random.randint( 0,255)
    b = random.randint( 0,255)
    t.fillcolor( r,g,b)
    t.hideturtle()
    draw_square(random.randint( 0, 200))
    t.showturtle()
    t.end_fill()

scr.exitonclick