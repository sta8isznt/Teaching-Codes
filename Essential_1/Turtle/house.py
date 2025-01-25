import turtle

# Set up the Turtle
my_turtle = turtle.Turtle()
my_turtle.speed(3)  # Set a moderate speed

# Draw the square base
for _ in range(4):
    my_turtle.forward(100)  # Length of the square's side
    my_turtle.left(90)

# Move to the top of the square
my_turtle.penup()  # Lift the pen to move without drawing
my_turtle.goto(0, 100)  # Move to the top of the square
my_turtle.pendown()  # Put the pen back down to draw

# Draw the triangle roof
my_turtle.goto(50, 150)  # Draw to the top of the roof
my_turtle.goto(100, 100)  # Draw to the other corner of the roof
my_turtle.goto(0, 100)  # Complete the triangle by returning to the starting point

# Finish
turtle.done()
