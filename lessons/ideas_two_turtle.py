"""A program to work out ideas for ex04."""

from turtle import Turtle, colormode, done
colormode(255)

# Christmas tree

a_turtle: Turtle = Turtle()
a_turtle.hideturtle()
a_turtle.speed(200)
a_turtle.color(27, 78, 9)
a_turtle.penup()
a_turtle.goto(90, 20)
a_turtle.pendown()

heading: int = 300
turn: int = 120
i: int = 0
i2: int = 0 
a_turtle.begin_fill()
while i2 < 2:
    i = 0
    while i < 4:
        a_turtle.setheading(heading)
        a_turtle.forward(50)
        a_turtle.right(turn)
        a_turtle.forward(10)
        i += 1
    a_turtle.forward(60)
    a_turtle.penup()
    a_turtle.goto(90, 20)
    a_turtle.pendown()
    heading = heading - 60
    turn = turn - 240
    i2 += 1
a_turtle.end_fill()

# Ornaments 
c_turtle: Turtle = Turtle()
c_turtle.hideturtle()
c_turtle.speed(200)
c_turtle.pencolor(27, 78, 9)
c_turtle.fillcolor(200, 77, 245)
c_turtle.penup()
c_turtle.goto(90, 20)
c_turtle.pendown()

heading: int = 300
turn: int = 120
i: int = 0
i2: int = 0 
dotsize: int = 12

while i2 < 2:
    i = 0
    while i < 4:
        c_turtle.setheading(heading)
        c_turtle.forward(50)
        c_turtle.dot(12, "purple")
        c_turtle.right(turn)
        c_turtle.forward(10)
        i += 1
    c_turtle.forward(60)
    c_turtle.penup()
    c_turtle.goto(90, 20)
    c_turtle.pendown()
    heading = heading - 60
    turn = turn - 240
    i2 += 1

# Star
b_turtle: Turtle = Turtle()
b_turtle.hideturtle()
b_turtle.speed(200)
b_turtle.fillcolor(242, 205, 76)
b_turtle.pencolor(245, 173, 77)
b_turtle.penup()
b_turtle.goto(110, 20)
b_turtle.pendown()

b_turtle.begin_fill()
i: int = 0
heading2: int = 288
b_turtle.begin_fill()
while i < 6:
    b_turtle.setheading(heading)
    b_turtle.forward(40)
    heading = heading - 180 - 36
    i += 1
b_turtle.end_fill()

done()