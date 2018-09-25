
import turtle

print("This program will draw a flower made of 7 hexagons with the user input of size and colors.")

length_side = input("Type the length of a side of a hexagon, in pixels: ")

color_center = input("Type the color of the center, in HEX: ")

color_petals = input("Type the color of the petals, in HEX: ")


def draw_hexagon():
    for x in range(6):
        turtle.forward(float(length_side))
        turtle.left(60)

turtle.speed(10)

turtle.color("black", color_center)

turtle.begin_fill()

draw_hexagon()

turtle.end_fill()

turtle.right(120)

turtle.color("black", color_petals)

for x in range(6):
    turtle.begin_fill()
    draw_hexagon()
    turtle.end_fill()
    turtle.right(120)
    turtle.forward(float(length_side))
    turtle.left(60)

turtle.exitonclick()
