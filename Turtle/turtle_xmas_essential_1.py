import turtle

turtle.setup(600, 600)
turtle.bgcolor("skyblue")
turtle.speed(0)

triangle_x_positions = [-100, -80, -60]
triangle_y_positions = [-200, -130, -80]
triangle_size = [200, 160, 120]

for i in range(3):
    turtle.penup()
    turtle.goto(triangle_x_positions[i], triangle_y_positions[i])
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    for j in range(3):
        turtle.forward(triangle_size[i])
        turtle.left(120)
    turtle.end_fill()

turtle.penup()
turtle.goto(-20, -200)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.fd(40)
    turtle.rt(90)
    turtle.fd(60)
    turtle.rt(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-20, 35)
turtle.pendown()
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle.fd(40)
    turtle.rt(144)
turtle.end_fill()

for i in range(3):
    turtle.penup()
    turtle.goto(triangle_x_positions[i], triangle_y_positions[i])
    turtle.pendown()
    turtle.dot(15, "red")

turtle.hideturtle()
turtle.done()

