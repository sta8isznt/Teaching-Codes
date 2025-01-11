import turtle

sam = turtle.Turtle()

for x in range(4):
    sam.forward(100)
    sam.right(90)

sam.goto((50, 50))
sam.goto((100, 0))

turtle.done()