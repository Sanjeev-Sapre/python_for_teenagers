import turtle
t= turtle.Turtle()
scr = turtle.getscreen()
x= -200
y=200

t.penup()
t.goto( x, y)
t.pendown()

def draw_square(side_length):
    t.goto(x,y)
    for i in range(4):
        t.forward( side_length)
        t.right(90)

# Part 1- instead of repeated typing, add this into loop, end loop till 50
# part 2- when new square starts , connecting line should not be there.
# hint - use pen up/down command.
draw_square(200)
x = x+5
y = y-5
draw_square(190)
x = x+5
y = y-5
draw_square(180)


#for i in range( 10, 100, 5):
 #   draw_square(i)

scr.exitonclick()