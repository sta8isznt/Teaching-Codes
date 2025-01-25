import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)  # Fastest speed

for i in range(100):
    my_turtle.forward(i * 5)  # Increase step size
    my_turtle.right(45)  # Turn 45 degrees

turtle.done()


#Challenge: Change the angle