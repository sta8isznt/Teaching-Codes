import turtle

# mai = turtle.Turtle()

# Set up the screen
turtle.setup(600, 600)
turtle.speed(0)
turtle.bgcolor("skyblue")

for i in range(3):
    if i == 0:
        size = 200
        x = -100
        y = -200
    elif i == 1:
        size = 160
        x = -80
        y =  -130 
    else:
        size = 120
        x = -60
        y = -80

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

turtle.penup()
turtle.goto(-20, -260)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
turtle.end_fill()


#Star design

turtle.penup()
turtle.goto(-15, 35)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle.forward(30)
    turtle.right(144)
turtle.end_fill()

# turtle.hideturtle()
turtle.done()