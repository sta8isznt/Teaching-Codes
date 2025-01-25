import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(5)  # Set the drawing speed
colors = ["red", "blue", "green", "yellow", "purple"]

for i in range(5):
    #my_turtle.color(colors[i])  # Change the pen color
    my_turtle.forward(150)
    my_turtle.right(144)  # Turn 144 degrees to make a star

turtle.done()

#Challenge: Experiment with colors and the size of the star