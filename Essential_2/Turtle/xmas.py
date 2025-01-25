import turtle
import random

def draw_triangle(color, size, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_rectangle(color, width, height, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_ornament(tree_x, tree_y, tree_width):
    x = random.randint(tree_x - tree_width // 2, tree_x + tree_width // 2)
    y = random.randint(tree_y - tree_width // 2, tree_y + tree_width // 2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(random.randint(5, 10), random.choice(["red", "blue", "yellow", "white", "gold", "pink"]))

def draw_star(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(20)
        turtle.right(144)
    turtle.end_fill()

# Set up the screen
turtle.setup(600, 600)
turtle.speed(0)
turtle.bgcolor("skyblue")

# Draw the tree layers
draw_triangle("green", 200, -100, -200)
draw_triangle("green", 160, -80, -130)
draw_triangle("green", 120, -60, -80)

# Draw the trunk
draw_rectangle("brown", 40, 60, -20, -260)

for _ in range(20):
    draw_ornament(0, -100, 200)  # Adjusted position to match the tree

# Draw the star
draw_star(-10, 35)  # Adjusted position to match the tree

# Hide turtle and display the drawing
turtle.hideturtle()
turtle.done()
