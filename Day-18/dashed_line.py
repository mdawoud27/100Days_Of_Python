from turtle import Turtle, Screen


# tim = Turtle()
# for _ in range(15):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")

tom = Turtle()
tom.pencolor("red")
tom.pensize(3)
# tom.pensize(4)
for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen = Screen()
screen.exitonclick()
