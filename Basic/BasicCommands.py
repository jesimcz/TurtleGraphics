# Overview of basic turtle commands  
# based on https://docs.python.org/3.3/library/turtle.html?highlight=turtle#module-turtle
#

import turtle

screen = turtle.Screen()

screen.bgcolor("light gray")

screen.screensize(1200, 900)

screen.title("Basic Turtle Graphics Commands")

t = turtle.Turtle()

t.setposition(0, 0)
t.width(4)

t.forward(100)



turtle.done()

