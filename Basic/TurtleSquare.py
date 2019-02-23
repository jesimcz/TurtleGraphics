# Python program to draw square using Turtle Programming 
# https://www.geeksforgeeks.org/turtle-programming-python/
#
import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")

skk = turtle.Turtle() 
  
for i in range(4): 
    skk.forward(50) 
    skk.right(90) 
      
turtle.done() 
