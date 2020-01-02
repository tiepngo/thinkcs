# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 09:57:17 2019

@author: WIN10
"""

import turtle

def regular_polygon(poly,size=50, n=4):
    print(type(poly))
    for i in range(n):
        poly.left(360/n)
        poly.forward(size)
        
wn = turtle.Screen()
tess = turtle.Turtle()
regular_polygon(tess,50,6)

wn.mainloop()