import turtle
import random
scr = turtle.getscreen()
t1= turtle.Turtle()
t2= turtle.Turtle()
scr.colormode(255)

x= -200
y =200




t1.hideturtle()
t2.hideturtle()
t1.speed(8)
t2.speed(2)
t1.goto( x, y)

def draw_square(side_length ):
    t1.goto(x,y)
    for i in range(4):
        t1.forward( side_length)
        t1.right(90)


def draw_circle(radious ):
      t2.circle(radious)


# Part 1- instead of repeated typing, add this into loop, end loop till 50
# part 2- when new square starts , connecting line should not be there.
# hint - use pen up/down command.
for i in range(50):
    draw_square(300)
    draw_circle( 100 +  ( i *5))
    x = x+5
    y = y-5

#for i in range( 10, 100, 5):
 #   draw_square(i)

scr.exitonclick()