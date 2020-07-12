import turtle
t= turtle.Turtle()
scr = turtle.getscreen()

def draw_square(side_length):
    for i in range(4):
        t.forward( side_length)
        t.right(90)


for i in range( 10, 100, 5):
    draw_square(i)

scr.exitonclick()