import turtle

# Ρύθμιση παραθύρου
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Απενεργοποίηση αυτόματης ενημέρωσης της οθόνης για καλύτερη απόδοση

# Σκορ
score_a = 0
score_b = 0

# Δημιουργία αριστερής ρακέτας
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Δημιουργία δεξιάς ρακέτας
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Δημιουργία μπάλας
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Ταχύτητα κίνησης στον άξονα x
ball.dy = 0.2  # Ταχύτητα κίνησης στον άξονα y

# Δημιουργία scoreboard
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Μεταβλητές για την κίνηση των paddles
left_paddle_speed = 0
right_paddle_speed = 0

# Κίνηση ρακέτας

def move_paddles():
    left_paddle.sety(left_paddle.ycor() + left_paddle_speed)
    right_paddle.sety(right_paddle.ycor() + right_paddle_speed)

    # Περιορισμός κινήσεων
    if left_paddle.ycor() > 250:
        left_paddle.sety(250)
    if left_paddle.ycor() < -240:
        left_paddle.sety(-240)
    if right_paddle.ycor() > 250:
        right_paddle.sety(250)
    if right_paddle.ycor() < -240:
        right_paddle.sety(-240)

# Χειρισμός εισόδων

def left_paddle_up():
    global left_paddle_speed
    left_paddle_speed = 10

def left_paddle_down():
    global left_paddle_speed
    left_paddle_speed = -10

def right_paddle_up():
    global right_paddle_speed
    right_paddle_speed = 10

def right_paddle_down():
    global right_paddle_speed
    right_paddle_speed = -10

def stop_left_paddle():
    global left_paddle_speed
    left_paddle_speed = 0

def stop_right_paddle():
    global right_paddle_speed
    right_paddle_speed = 0

# Αντιστοίχιση πλήκτρων στο πληκτρολόγιο
wn.listen()
wn.onkeypress(left_paddle_up, "w")
wn.onkeyrelease(stop_left_paddle, "w")
wn.onkeypress(left_paddle_down, "s")
wn.onkeyrelease(stop_left_paddle, "s")
wn.onkeypress(right_paddle_up, "Up")
wn.onkeyrelease(stop_right_paddle, "Up")
wn.onkeypress(right_paddle_down, "Down")
wn.onkeyrelease(stop_right_paddle, "Down")

# Ενημέρωση σκορ

def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Κύριος βρόχος του παιχνιδιού
while True:
    wn.update()
    move_paddles()
    
    # Κίνηση μπάλας
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Έλεγχος σύγκρουσης με τα όρια του παραθύρου
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Αντιστροφή κατεύθυνσης
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    # Έλεγχος αν η μπάλα βγει εκτός δεξιά ή αριστερά
    global score_a, score_b
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  # Επαναφορά μπάλας στο κέντρο
        score_a += 1
        update_score()
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        update_score()
    
    # Έλεγχος σύγκρουσης με τις ρακέτες
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
