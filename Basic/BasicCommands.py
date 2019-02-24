# Overview of basic turtle commands  
# based on https://docs.python.org/3.3/library/turtle.html?highlight=turtle#module-turtle
#

import turtle

screen = turtle.Screen()

screen.bgcolor("light gray")

#screen.screensize(1200, 900)
screen.setup (width=1200, height=900, startx=0, starty=0)

screen.title("Basic Turtle Graphics Commands")

t = turtle.Turtle()

t.setposition(0, 0)
t.width(1)

t.forward(100)

t.width(1)
t.left(90)
t.forward(200)

t.penup()
t.setposition(0, 0)
t.pendown()
t.write("0,0", False, align="left")

t.penup()
t.setposition(500, 0)
t.pendown()
t.write("500,0", False, align="left")

t.penup()
t.setposition(500, 500)
t.pendown()
t.write("500,500", False, align="left")

turtle.done()

