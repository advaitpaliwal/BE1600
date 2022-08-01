import turtle
t = turtle.Turtle()


def drawSquares(s_len, gap):

    for i in range(10):

        for j in range(4):
            t .forward(s_len)
            t .left(90)

        x, y = t .position()

        t.penup()
        t.goto(x + gap / 2, y + gap / 2)
        t.pendown()

        s_len -= gap

    turtle.done()


drawSquares(150, 10)
