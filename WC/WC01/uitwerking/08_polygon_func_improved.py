import turtle
don = turtle.Turtle()


def polygon(turt, sides, size=100):
    for step in range(sides):
        turt.forward(size)
        turt.left(360 / sides)


for shape in range(90):
    polygon(don, 6)
    don.left(4)
