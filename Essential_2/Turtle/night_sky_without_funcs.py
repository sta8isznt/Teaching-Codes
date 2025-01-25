import turtle
import random

# Set up the screen and Turtle
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
my_turtle = turtle.Turtle()
my_turtle.speed(0)  # Fastest speed
my_turtle.hideturtle()  # Hide the Turtle

# Generate random stars
for _ in range(100):  # Create 50 stars
    x = random.randint(-600, 600)  # Random X-coordinate
    y = random.randint(-600, 600)  # Random Y-coordinate
    size = random.randint(10, 30)  # Random size
    color = random.choice(["white", "yellow", "lightblue"])

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.color(color)
    for _ in range(5):  # Draw a star
        my_turtle.forward(size)
        my_turtle.right(144)

# Finish
turtle.done()