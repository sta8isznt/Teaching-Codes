import turtle

# Set up the screen and Turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.speed(0)  # Fastest speed

# Function to draw a circle with patterns
def draw_mandala():
    colors = ["red", "blue", "green", "purple", "orange"]
    for i in range(36):  # Repeat to complete the circular design
        my_turtle.color(colors[i % len(colors)])  # Cycle through colors
        my_turtle.circle(100)  # Draw a circle
        my_turtle.right(10)  # Rotate the drawing by 10 degrees

# Draw the mandala
draw_mandala()

# Finish
turtle.done()
