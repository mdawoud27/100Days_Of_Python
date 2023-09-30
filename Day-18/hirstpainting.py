import colorgram
import turtle
import random


def extract_image_colors(image_name, extracted_number):
    colors = colorgram.extract(image_name, extracted_number)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    # Removing the first THREE transparent colors
    new_colors = rgb_colors[3:]
    return new_colors


def starting_point():
    tim.setheading(220)
    tim.forward(350)
    tim.setheading(0)


def set_starting_point():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = extract_image_colors("image.jpg", 30)

starting_point()

# Line length
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

set_starting_point()

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
