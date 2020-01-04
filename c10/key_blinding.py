import turtle

wn = turtle.Screen()

tess = turtle.Turtle()

def color_red():
    tess.color("red")

def color_yellow():
    tess.color("yellow")

def color_blue():
    tess.color("blue")

def test():
    tess.forward(30)

pen_size = 1

def pen_size_inc():
    global pen_size
    if 0 < pen_size < 21 :
        wn.title("Pen size : {}".format(pen_size))
        pen_size +=1
        tess.pensize(pen_size)

def pen_size_dec():
    global pen_size
    if 0 < pen_size < 21 :
        wn.title("Pen size : {}".format(pen_size))
        pen_size -=1
        tess.pensize(pen_size)

wn.onkey(color_blue,"b")
wn.onkey(color_red, "r")
wn.onkey(color_yellow, "y")
wn.onkey(pen_size_dec, "-")
wn.onkey(pen_size_inc, "+")

wn.onkey(test, "space")
wn.listen()
wn.mainloop()