import turtle

turtle.setup(800, 800)
turtle.speed(0)
turtle.bgcolor("skyblue")
nikos = turtle.Turtle()

colors = ["green", "red", "yellow", "blue", "orange", "purple"]
for i in range(36):
    color = colors[i % len(colors)]

