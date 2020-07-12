import turtle

t = turtle.Pen()

t.color( 1,0,0)
def mystar(size, filled):
        if filled == True:
            t.begin_fill()
        for x in range(1, 19):
            t.forward(size)
            if x % 2 == 0:
                t.left(175)
            else:
                t.left(125)
        if filled == True:
            t.end_fill()


def myc(r,g,b,d) :
	t.color( r,g,b)
	t.begin_fill()
	t.circle(d)
	t.end_fill()

mystar(200, True)
