# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 13:43:26 2019

@author: WIN10
"""

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

def draw_square(t, size):
    for i in range(4):
        t.left(90)
        t.forward(size)

def draw_innter(t, size, delta, n):
    for i in range(n):
        draw_square(tess, size)
        tess.penup()
        tess.forward(delta)
        tess.right(90)
        tess.forward(20)
        tess.left(90)
        tess.pendown()
        size += delta*2
tess.speed(5)
draw_innter(tess, 50, 20,5)
wn.mainloop()