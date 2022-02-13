"""EX04 - A Turtle Scene Exercise.

My idea of hygge is Christmas, which I have created in my scene. In the turtle I am drawing a Christmas tree which is 
placed at x, y from the top of the tree. The tree is decorated by ornaments and a star, which are seperate function that
are used within the Christmas tree function. Also, there are two functions for making hearts, one is the drawing of an 
individul heart and one is a 'helper' that draws a heart a given amount of times randomly located. 
I have attempted to break down procedures by creating functions that print different objects but are then used in another 
function, as well as divided the printing of random located hearts by using two functions. 
I have also tried implementing additional turtle functions like color background, dot and circle.
""" 
__author__ = "730464966"

from turtle import Turtle, bgcolor, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint for my scene program."""
    a_turtle: Turtle = Turtle()
    a_turtle.hideturtle()
    # Adding a light blue background.
    bgcolor(169, 218, 222)
    # "Opens" first function for drawing objects
    christmas_tree(a_turtle, 0, 0)
    many_hearts(6)


def christmas_tree(turtle: Turtle, x: float, y: float) -> None:
    """Draw christmas tree that located at x, y from the tree's top. Uses two other functions to draw ornaments and a star on the tree."""
    # Turtle variable for christmas tree, with color green and starting point x,y
    a_turtle: Turtle = Turtle()
    a_turtle.hideturtle()
    a_turtle.speed(200)
    a_turtle.color(27, 78, 9)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    heading: int = 300
    turn: int = 120
    i: int = 0
    i2: int = 0 

    a_turtle.begin_fill()
    # While loops used to simplefy the coding for drawing each of the sides and each zigzag
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
        a_turtle.goto(x, y)
        a_turtle.pendown()
        heading = heading - 60
        turn = turn - 240
        i2 += 1
    a_turtle.end_fill()
    # "Opening" the next function where the start point x, y is used to draw ornanments on the tree"
    b_turtle: Turtle = Turtle()
    b_turtle.hideturtle()
    ornaments(b_turtle, x, y)
    # "Opening" the next function where the start point x, y is used to draw a star on the tree"
    c_turtle: Turtle = Turtle()
    c_turtle.hideturtle()
    star(c_turtle, x, y)
    

def star(turtle: Turtle, x: float, y: float) -> None:
    """Drawing a star at the top of the tree top by using x,y."""
    # Turtle variable for the star, with color yellow
    c_turtle: Turtle = Turtle()
    c_turtle.hideturtle()
    c_turtle.speed(200)
    c_turtle.fillcolor(242, 205, 76)
    c_turtle.pencolor(245, 173, 77)
    c_turtle.penup()
    # The starting point is a shifted so it fits with the top of the tree
    c_turtle.goto(x - 10, y + 10)
    c_turtle.pendown()

    c_turtle.begin_fill()
    i: int = 0
    heading: int = 288
    c_turtle.begin_fill()
    while i < 6:
        c_turtle.setheading(heading)
        c_turtle.forward(40)
        # Using that the stars point have a 36 degree angle.
        heading = heading - 180 - 36
        i += 1
    c_turtle.end_fill()


def ornaments(turtle: Turtle, x: float, y: float) -> None:
    """Drawing ornaments on the christmas tree."""
    b_turtle: Turtle = Turtle()
    b_turtle.hideturtle()
    b_turtle.speed(200)
    b_turtle.pencolor(27, 78, 9)
    b_turtle.fillcolor(200, 77, 245)
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.pendown()

    heading: int = 300
    turn: int = 120
    i: int = 0
    i2: int = 0 

    while i2 < 2:
        # Using similar while loop to create the ornaments by tracing the sides of the tree
        i = 0
        while i < 4:
            b_turtle.setheading(heading)
            b_turtle.forward(50)
            b_turtle.dot(12, "purple")
            b_turtle.right(turn)
            b_turtle.forward(10)
            i += 1
        b_turtle.forward(60)
        b_turtle.penup()
        b_turtle.goto(x, y)
        b_turtle.pendown()
        heading = heading - 60
        turn = turn - 240
        i2 += 1


def hearts(turtle: Turtle, x: int, y: int) -> None:
    """Drawing hearts located at x,y."""
    # Turtle variable with color red
    d_turtle: Turtle = Turtle()
    d_turtle.hideturtle() 
    d_turtle.speed(200)
    d_turtle.color(201, 58, 47)
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.pendown()

    # The drawing of the heart using straight lines and circles
    d_turtle.begin_fill()
    d_turtle.setheading(350)
    d_turtle.circle(9, None, None)
    d_turtle.setheading(295)
    d_turtle.forward(20)
    d_turtle.setheading(65)
    d_turtle.forward(20)
    d_turtle.setheading(10)
    d_turtle.circle(9, None, None)
    d_turtle.setheading(150)
    d_turtle.forward(10)
    d_turtle.setheading(210)
    d_turtle.forward(10)
    d_turtle.end_fill()


def many_hearts(total_hearts: int) -> None:
    """Print hearts the amount of times the user imputs into function and place them randomly in turtle window."""
    i: int = 0
    e_turtle: Turtle = Turtle()
    e_turtle.hideturtle()
    # Using the randint function to print the hearts at random places in turtle scene
    from random import randint
    while i < total_hearts:
        hearts(e_turtle, randint(-250, 250), randint(-250, 250))
        i += 1


if __name__ == "__main__":
    print("__name is '__main__")
    main()

done()