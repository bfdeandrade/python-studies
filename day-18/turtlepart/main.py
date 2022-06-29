from turtle import Turtle, Screen
from data import shapes_dict
from random import randrange
timmy_turtle = Turtle()


screen = Screen()
screen.colormode(255)
timmy_turtle.shape("turtle")
timmy_turtle.turtlesize(2, 2, 2)

def draw_square():
    for _ in range(4):
        timmy_turtle.left(90)
        timmy_turtle.forward(60)

def draw_dashed_line():
    for _ in range(10):
        timmy_turtle.pen(pendown=True,pensize=1)
        timmy_turtle.forward(10)
        timmy_turtle.pen(pendown=False,pensize=1)
        timmy_turtle.forward(10)
def draw_multiple_shapes(sides, size):
    for key, value in sides.items():
        timmy_turtle.pen(pencolor=(randrange(0,255),randrange(0,255),randrange(0,255)))
        for i in range(value):
            timmy_turtle.left(360 / value)
            timmy_turtle.forward(size)

def draw_random_walk():
    timmy_turtle.pen(speed=5)
    while True:
        timmy_turtle.pen(pencolor=(randrange(0,255),randrange(0,255),randrange(0,255)), pensize=15)
        random_walk = randrange(0,60)
        random_angle = randrange(0, 270, 90)
        timmy_turtle.forward(random_walk)
        timmy_turtle.setheading(random_angle)

def draw_spirograph(size_of_gap, radius):
    for _ in range(int(360 / size_of_gap)):
        timmy_turtle.pen(pencolor=(randrange(0,255),randrange(0,255),randrange(0,255)), pensize=1, speed=10)
        timmy_turtle.circle(radius)
        timmy_turtle.setheading(timmy_turtle.heading() + size_of_gap)

draw_spirograph(5, 50)

screen.exitonclick()