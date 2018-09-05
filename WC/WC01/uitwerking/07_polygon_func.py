import turtle
don = turtle.Turtle()


def polygon(sides):
    for step in range(sides):
        don.forward(100)
        don.left(360 / sides)


for shape in range(90):
    polygon(6)
    don.left(4)