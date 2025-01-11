import turtle

nikos = turtle.Turtle()
nikos.speed(0)
colors = ["black", "purple", "blue", "red", "green"]
turtle.bgcolor("skyblue")

for i in range(5):
    nikos.color(colors[i])
    nikos.forward(200)
    nikos.right(144)

turtle.done()