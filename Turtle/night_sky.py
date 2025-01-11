import turtle
import random

# Set up the screen
turtle.bgcolor("black")
nikos = turtle.Turtle()
nikos.speed(0)
nikos.hideturtle()

colors = ['white', 'yellow', 'lightblue', 'orange']

for i in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(10, 40)

    nikos.penup()
    nikos.goto(x, y)
    nikos.pendown()
    color = random.choice(colors)
    nikos.color(color)
    nikos.fillcolor(color)
    nikos.begin_fill()
    for i in range(5):
        nikos.forward(size)
        nikos.right(144)
    nikos.end_fill()


turtle.done()