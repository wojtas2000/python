import turtle


def ramie():
    turtle.forward(100)
    for x in range(0, 4):
        turtle.forward(100)
        turtle.left(90)
    turtle.forward(100)


for x in range(0, 4):
    ramie()
    turtle.right(90)

turtle.done()
