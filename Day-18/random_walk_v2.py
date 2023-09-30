import random
import turtle as tt

tim = tt.Turtle()
tt.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple_color = (r, g, b)
    return tuple_color


tim_directions = [0, 90, 180, 270]
tim.speed("fastest")
tim.pensize(5)

for _ in range(100):
    tim.color(random_color())
    tim.forward(15)
    tim.setheading(random.choice(tim_directions))

screen = tt.Screen()
screen.exitonclick()
