import random
from turtle import Turtle, Screen

tim = Turtle()
tim_colors = ["#483D8B", "#FF4500", "#FFA07A", "#C71585", "#000000", "#2F4F4F", "#FFFF00", "#006400", "#FF0000",
              "#4B0082", "#FF00FF", "#FFA500", "#8B0000", "#00FFFF", "#5F9EA0"]
tim_directions = [0, 90, 180, 270]
tim.speed("fastest")
tim.pensize(5)

for _ in range(500):
    tim.color(random.choice(tim_colors))
    tim.forward(15)
    tim.setheading(random.choice(tim_directions))

screen = Screen()
screen.exitonclick()
