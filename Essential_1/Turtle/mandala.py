import turtle

turtle.setup(800, 800)
turtle.speed(0)
turtle.bgcolor("skyblue")
turtle.hideturtle()
colors = ["green", "red", "yellow", "blue", "orange", "purple"]
for i in range(72):
    color = colors[i % len(colors)]
    turtle.color(color)
    turtle.circle(100)
    turtle.right(5)

turtle.done()
