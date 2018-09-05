import turtle
don = turtle.Turtle()


def polygon(turt, sides, size=100):
    for step in range(sides):
        turt.forward(size)
        turt.left(360 / sides)


for step in range(90):
    if (step % 2) == 1:
        don.color('red')
    else:
        don.color('blue')
    polygon(don, 5)
    don.left(360 / 90)


