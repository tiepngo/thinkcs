import turtle
turtle.setup(400,400)
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.shape("circle")
tess.color("purple")

def h1(x,y):
    tess.goto(x,y)

wn.onclick(h1)
wn.mainloop()