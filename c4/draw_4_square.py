# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 11:26:10 2019

@author: WIN10
"""

import turtle

def square(t,size):
    for i in range(4):
        t.right(90)
        t.forward(size)

def draw_square(t,size,n):
    for i in range(n):
        print("Square number : ", i)
        square(t,size)
        t.forward(size*2)

w = turtle.Screen()
tess = turtle.Turtle()
tess.color("blue")
tess.speed(10)

draw_square(tess,100,5)
w.mainloop()