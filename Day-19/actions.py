from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Define functions for each action
def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Create a dictionary of key-function mappings
actions = {
    "w": move_forward,
    "s": move_backward,
    "a": turn_left,
    "d": turn_right,
    "c": clear_screen
}

# Set up key bindings for each action
for key, action in actions.items():
    screen.onkey(key=key, fun=action)

# Listen for key events
screen.listen()

# Close the screen when clicked
screen.exitonclick()
