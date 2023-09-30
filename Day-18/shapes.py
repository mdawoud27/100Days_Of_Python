import random
from turtle import Turtle, Screen

tim = Turtle()
tim_colors = ["#483D8B", "#FF4500", "#FFA07A", "#C71585", "#000000", "#2F4F4F", "#FFFF00"]


def draw_shape(side_num):
    for _ in range(side_num):
        tim.forward(100)
        tim.right(360 / side_num)


for shape_side_n in range(3, 11):
    tim.color(random.choice(tim_colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
