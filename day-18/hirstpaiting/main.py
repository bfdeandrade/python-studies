from curses import color_content
from turtle import Turtle, Screen
import colorgram
from random import choice


colors_list = list()
colors = colorgram.extract('hirst.jpg', 6)

for color in colors:
    rgb = color.rgb 
    r, g, b = rgb.r, rgb.g, rgb.b
    tuple_rgb  = (r, g, b)
    colors_list.append(tuple_rgb)


tim = Turtle()
tim.shape("arrow")
screen = Screen()
screen.colormode(255)
def draw_dots(size_of_dot, size_of_gap, color_list):
    for pos in range(0, 500, 50):
        tim.setposition(0,pos)
        for i in range(10):
            tim.dot(size_of_dot, choice(colors_list))
            tim.pu()
            tim.forward(50)


draw_dots(10, 50, colors_list)

screen.exitonclick()