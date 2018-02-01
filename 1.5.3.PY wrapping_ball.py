#####
# bouncing_ball.py
# 
# Creates a Scale and a Canvas. Animates a circle based on the Scale
# (c) 2013 PLTW
# version 11/1/2013
####

import Tkinter #often people import Tkinter as *
import random
import math
#####
# Create root window 
####
root = Tkinter.Tk()

#####
# Create Model
######
speed_intvar = Tkinter.IntVar()
speed_intvar.set(3) # Initialize y coordinate
# radius and x-coordinate of circle
blue_intvar = Tkinter.IntVar()
blue_intvar.set(255)
r = 10
x = 150
y = 150
direction = random.uniform(0,2*math.pi) # radians of angle in standard position, ccw from positive x axis
 
######
# Create Controller
#######
# Instantiate and place slider
speed_slider = Tkinter.Scale(root, from_=5, to=1, variable=speed_intvar,    
                              label='speed')
speed_slider.grid(row=1, column=0, sticky=Tkinter.W)

blue_slider = Tkinter.Scale(root, from_=0, to=255, variable=blue_intvar, label='blue level')
blue_slider.grid(row=3, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\nspeed.')
text.grid(row=0, column =0)

text2 = Tkinter.Label(root, text='Drag slider \nto adjust\nblue color.')
text2.grid(row=2, column =0)
######
# Create View
#######
# Create and place a canvas
canvas = Tkinter.Canvas(root, width=600, height=600, background='#FFFFFF')
canvas.grid(row=0, rowspan=4, column=1)

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
def animate():
    # Get the slider data and create x- and y-components of velocity
    velocity_x = speed_intvar.get() * math.cos(direction) # adj = hyp*cos()
    velocity_y = speed_intvar.get() * math.sin(direction) # opp = hyp*sin()
    # Change the canvas item's coordinates
    canvas.move(circle_item, velocity_x, velocity_y)
    canvas.itemconfig(circle_item, fill = '#00FF' + hexIt(blue_intvar))
    
    # Get the new coordinates and act accordingly if ball is at an edge
    x1, y1, x2, y2 = canvas.coords(circle_item)
    global direction
    # If crossing left or right of canvas
    if x2>canvas.winfo_width(): 
        canvas.move(circle_item, -615, 0) 
    if x1<0:
        canvas.move(circle_item, 615, 0) 
    # If crossing top or bottom of canvas
    if y2>canvas.winfo_height(): 
        canvas.move(circle_item, 0, -615)
    if y1<0:
        canvas.move(circle_item, 0, 615)
    # Create an event in 1 msec that will be handled by animate(),
    # causing recursion        
    canvas.after(1, animate)

def hexIt(color_intvar):
    color_int = color_intvar.get()
    slider_hex = hex(color_int)
    slider_hex_digits = slider_hex[2:]
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits
    return slider_hex_digits
    
animate()
#######
# Event Loop
#######
root.mainloop()