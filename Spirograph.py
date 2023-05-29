"""CS 108 - Lab 5.2

Drawing a spirograph using python.

@author: Blessing Amoah (bsa5)
@date: Fall, 2022
"""
from guizero import App, Drawing
import math

def draw_spirograph():
    # Indicate input information
    r = float(input("Moving radius: "))
    R = float(input("Fixed radius: "))
    p = float(input("Pen offset: "))
    color = input("Color: ")

    # Create the app and drawing
    app = App('Drawing Canvas')
    drawing = Drawing(app, width='fill', height='fill')

    t = 0.0
    center = app.width / 2

    x = (R + r) * math.cos(t) + p * math.cos((R + r) * t / r) + center
    y = (R + r) * math.sin(t) + p * math.sin((R + r) * t / r) + center
    while t < 360:
        t = t + 0.1

        next_x = (R + r) * math.cos(t) + p * math.cos((R + r) * t / r) + center
        next_y = (R + r) * math.sin(t) + p * math.sin((R + r) * t / r) + center

        drawing.line(x, y, next_x, next_y, color=color)
        x = next_x
        y = next_y
        app.update()

    app.display()

draw_spirograph()
