import turtle
turtle.setup(400,400)
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

def h1():
    tess.forward(30)

def h2():
    tess.right(45)

def h3():
    tess.left(45)

def h4():
    wn.bye()

wn.onkey(h1, "Up")
wn.onkey(h2, "Right")
wn.onkey(h3, "Left")
wn.onkey(h4, "q")

wn.listen()
wn.mainloop()