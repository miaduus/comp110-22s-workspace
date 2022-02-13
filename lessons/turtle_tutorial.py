"""Tutorial in using turtle."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()

leo.pencolor(18, 44, 165)
leo.fillcolor(126, 212, 227)
leo.penup()
leo.goto(0, 0)
leo.pendown()

side_lenght: float = 100

leo.begin_fill()
i: int = 0
while (i < 6):
    leo.forward(side_lenght)
    leo.right(60)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.speed(400)
bob.hideturtle()
bob.color(8, 8, 8)

bob.penup()
bob.goto(0, 0)
bob.pendown()

i: int = 0
while (i < 120):
    side_lenght = side_lenght * 0.96
    bob.forward(side_lenght)
    bob.right(61)
    i += 1
done()