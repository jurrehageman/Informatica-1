import turtle
don = turtle.Turtle()
for hexagon in range(90):
    for step in range(6):
        don.forward(100)
        don.left(60)
    don.left(4)