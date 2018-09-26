
import turtle


def give_instruction():
    print("This program will draw a flower made of 7 hexagons with the user input of size and colors.")


def input_length():
    length_side = input("Type the length of a side of a hexagon, in pixels: ")
    return length_side


def input_color_center():
    color_center = input("Type the color of the center, in HEX: ")
    return color_center


def input_color_petals():
    color_petals = input("Type the color of the petals, in HEX: ")
    return color_petals


def draw_hexagon(length_side, color):
    turtle.color("black", color)
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(float(length_side))
        turtle.left(60)
    turtle.end_fill()


def main():
    give_instruction()
    length_side = input_length()
    color_center = input_color_center()
    color_petals = input_color_petals()

    turtle.speed(10)

    draw_hexagon(length_side, color_center)

    turtle.right(120)
    # rearranging where turtle is facing before starting the loop

    for x in range(6):
        draw_hexagon(length_side, color_petals)

        turtle.right(120)
        turtle.forward(float(length_side))
        turtle.left(60)
        # rearranging turtle before drawing the next petal

    turtle.exitonclick()


main()
