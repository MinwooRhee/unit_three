

def main():
    import turtle

    print("This program will draw a flower made of 7 hexagons with the user input of size and colors.")

    length_side = input("Type the length of a side of a hexagon, in pixels: ")

    color_center = input("Type the color of the center, in HEX: ")

    color_petals = input("Type the color of the petals, in HEX: ")

main()

def draw_hexagon:
    for x in range (6):
        turtle.foward(float(length_side))
        turtle.right(60)