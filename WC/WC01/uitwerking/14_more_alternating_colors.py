import turtle
don = turtle.Turtle()


def polygon(turt, sides, size=100):
    for step in range(sides):
        turt.forward(size)
        turt.left(360 / sides)


colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta']

for step in range(70):
    index = step % len(colors)
    color = colors[ index ]
    don.color(color)
    polygon(don, 6)
    don.left(360 / 70)

