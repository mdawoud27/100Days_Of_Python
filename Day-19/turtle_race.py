import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["blue", "orange", "yellow", "green", "black", "cyan"]
all_turtles = []

i = 0
for turtle_idx in range(90, -61, -30):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=turtle_idx)
    new_turtle.color(colors[i])
    i += 1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()
