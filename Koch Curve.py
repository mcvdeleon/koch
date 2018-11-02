# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:55:07 2018

@author: Monica
"""

from turtle import*

#First, give the parameters of the Koch triangle
# order represents the order and length is the base lenth of the first equilateral triangle

order = 3
length = 250

#Finish setting up the turtle by assigning its movements (penup and pendown) and its speed

fractal = Turtle()
speed(0)

def koch(t, side, order):
  if order == 0:
    # Just draw a segment
    fd(side)
  else:
    side = side/3.0
    # Make each straight bit into a smaller version of ourselves
    koch(t, side, order - 1)
    left(60)
    koch(t, side, order - 1)
    right(120)
    koch(t, side, order - 1)
    left(60)
    koch(t, side, order - 1)



koch(fractal, length, order)
mainloop()
