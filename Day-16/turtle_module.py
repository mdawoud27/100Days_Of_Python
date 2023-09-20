#!/uer/bin/python3
from turtle import *

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
timmy.goto(30, 50)
print(timmy.position())

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
# my_screen.bgcolor("coral")
my_screen.exitonclick()
print(type(my_screen))
