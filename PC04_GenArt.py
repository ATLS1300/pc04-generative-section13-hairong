# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:42:01 2021

@author: 74772
"""
# Description: Circles on Circles
# Create a gradient color background
# and use random function to draw random circles in three columns of the screen and in random colors

import turtle, random

turtle.clear()
turtle.colormode(255)
turtle.speed(10)
turtle.up()


panel=turtle.Screen()
w=600
h=600
panel.setup(width=w,height=h)

panel.bgcolor("#fff1e6")
        
Window = turtle.Turtle()
Window.width(60)
palette=["#eae4e9","#fff1e6","#fde2e4","#fad2e1","#e2ece9","#bee1e6","#f0efeb","#dfe7fd","#cddafd","#D2DDFD"]
for i in range(10): #range 10 to access to the ten colors in the palette 
    Window.pencolor(palette[i])
    Window.circle(50*i)
    Window.up()
    Window.sety((50*i)*(-1))
    Window.down()


circle=turtle.Turtle()
xAxis = [-225,0,225] #set the x-axis location to locate the circle

for i in xAxis: #access to each of the three columns
    for j in range(0,15): #draw the circles on each columns 15 times
        location = list(range(-300,300))
        y=random.choice(location) #select random y-axis location on the screen
        ramRadius = list(range(1,75))
        radius=random.choice(ramRadius) #use random function to randomize the radius of each circle
        
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb= [r,g,b]     #use random function to choose random color in RGB code
        circle.pensize(10)
        circle.pencolor(rgb)
        
        circle.hideturtle()
        circle.up()
        circle.goto(i,y)
        circle.down()
        circle.circle(radius)
        j=j+1
        
