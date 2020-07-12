import turtle
import random
t= turtle.Turtle()
scr = turtle.getscreen()
x= -200
y=200

scr.colormode(255)



t.penup()
t.goto( x, y)
t.pendown()

def draw_square(side_length):
    t.goto(x,y)
    r = random.randint(128,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.pencolor( r,g,b)
    for i in range(4):
        t.forward( side_length)
        t.right(90)

# Part 1- instead of repeated typing, add this into loop, end loop till 50
# part 2- when new square starts , connecting line should not be there.
# hint - use pen up/down command.
for i in range(50):
    draw_square(300)
    x = x+5
    y = y-5

#for i in range( 10, 100, 5):
 #   draw_square(i)

scr.exitonclick()