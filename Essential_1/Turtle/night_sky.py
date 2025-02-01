import turtle, random

turtle.bgcolor("black") # Βάζει χρώμα φόντου
turtle.setup(600, 600) # Ρυθμίζει μέγεθος παραθύρου
turtle.speed(0) # Αυξάνουμε την ταχύτητα
turtle.hideturtle() # Κρύβει τη χελώνα
colors = ["skyblue", "yellow", "red", "white"] # Λίστα από χρώματα

for i in range(50):
    #random x, y, size, color
    x = random.randint(-300, 300) # Ορίζουμε τυχαίο σημείο για το αστέρι μας
    y = random.randint(-300, 300)
    size = random.randint(10, 30) 
    color = random.choice(colors)

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    for j in range(5):
        turtle.fd(size)
        turtle.rt(144)



turtle.done()