from curses import color_content
from turtle import color
import colorgram


colors_list = list()
colors = colorgram.extract('hirst.jpg', 6)

for color in colors:
    rgb = color.rgb 
    r, g, b = rgb.r, rgb.g, rgb.b
    tuple_rgb  = (r, g, b)
    colors_list.append(tuple_rgb)
print(colors_list)