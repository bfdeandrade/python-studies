#WIP, going back after 
from turtle import Turtle


class TurtleMutant(Turtle):
    def __init__(self):
        print("Turtle Mutant!!!")

    def draw_square():
        for _ in range(4):
            Turtle.left(90)
            Turtle.forward(60)

    def draw_dashed_line():
        for _ in range(10):
            Turtle.pen(pendown=True,pensize=1)
            Turtle.forward(10)
            Turtle.pen(pendown=False,pensize=1)
            Turtle.forward(10)
    def draw_multiple_shapes(sides, size):
        for key, value in sides.items():
            for i in range(value):
                Turtle.left(360 / value)
                Turtle.forward(size)