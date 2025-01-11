import turtle

nikos = turtle.Turtle()
nikos.speed(0)
turtle.bgcolor('skyblue')

colors = ['red', 'blue', 'green', 'purple', 'orange']
for i in range(36):
    nikos.color(colors[i%5])
    nikos.circle(100)
    nikos.rt(10)

turtle.done()