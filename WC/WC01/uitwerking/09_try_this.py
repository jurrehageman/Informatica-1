import turtle
don = turtle.Turtle()


def polygon(turt, sides, size=100):
    for step in range(sides):
        turt.forward(size)
        turt.left(360 / sides)


def first():
    for size in range(90):
        polygon(don, 7, size)
        don.left(4)


def second():
    for sides in range(3, 9):
        polygon(don, sides)
        don.left(60)


def third():
    for sides in range(3, 12, 2):
        polygon(don, sides)
        don.left(72)


first()
#second()
#third()

