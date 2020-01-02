# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 14:02:11 2019

@author: WIN10
"""

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_square(t, size):
    for i in range(4):
        t.left(90)
        t.forward(size)

def pretty_pattern(t, size, n):
    for i in range(n):
        draw_square(tess, size)
        tess.left(360/n)

tess.color("blue")
pretty_pattern(tess, 100, 20 )
wn.mainloop()