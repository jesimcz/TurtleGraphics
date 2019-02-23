# Python program to draw  Spiral Square Outside In and Inside Outusing Turtle Programming 
# https://www.geeksforgeeks.org/turtle-programming-python/
#
import turtle   #Outside_In 
wn = turtle.Screen() 
wn.bgcolor("light gray") 
wn.title("Turtle Grphics - Spiral") 
skk = turtle.Turtle() 
skk.color("black") 
  
def sqrfunc(size): 
    for i in range(4): 
        skk.fd(size) 
        skk.left(90) 
        size = size-5
  
sqrfunc(146) 
sqrfunc(126) 
sqrfunc(106) 
sqrfunc(86) 
sqrfunc(66) 
sqrfunc(46) 
sqrfunc(26)
