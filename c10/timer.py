import turtle

turtle.setup(400,400)
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

def h1():
    ''' The timer only run once'''
    tess.forward(60)
    tess.left(45)

def h1_correct():
    tess.forward(60)
    tess.left(45)
    wn.ontimer(h1_correct, 2000)

h1_correct()
#wn.ontimer(h1, 2000)
wn.mainloop()