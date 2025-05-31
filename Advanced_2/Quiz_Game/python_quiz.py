import random
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

questions = [
    {
        "question": "Τι κάνει η εντολή pygame.init();",
        "options": ["A. Ξεκινάει το παιχνίδι", "B. Φορτώνει το player", "C. Εκκινεί τις μονάδες του Pygame", "D. Δημιουργεί το παράθυρο"],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Ποια εντολή χρησιμοποιούμε για να δημιουργήσουμε οθόνη στο Pygame;",
        "options": ["A. pygame.screen()", "B. pygame.set_mode()", "C. pygame.display()", "D. pygame.draw_screen()"],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Τι τύπου αντικείμενο είναι το screen στο Pygame;",
        "options": ["A. string", "B. int", "C. surface", "D. canvas"],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Πώς ελέγχουμε αν ο παίκτης έκλεισε το παράθυρο;",
        "options": ["A. event.type == pygame.CLOSE", "B. event == QUIT", "C. event.type == pygame.QUIT", "D. quit(event)"],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Ποια συνάρτηση χρωματίζει την οθόνη;",
        "options": ["A. fill()", "B. draw()", "C. color()", "D. paint()"],
        "answer": "A",
        "difficulty": "easy"
    },
    {
        "question": "Πώς σχεδιάζουμε ένα κύκλο στο Pygame;",
        "options": ["A. draw.circle()", "B. pygame.draw.circle()", "C. pygame.circle()", "D. drawCircle()"],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Ποια βιβλιοθήκη εισάγουμε για το Pygame;",
        "options": ["A. import game", "B. import pygame", "C. include pygame", "D. pygame.load"],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Τι επιστρέφει η pygame.key.get_pressed();",
        "options": ["A. Το πλήκτρο που πατήθηκε", "B. Λίστα με True/False για κάθε πλήκτρο", "C. String με το πλήκτρο", "D. Τίποτα"],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Ποια εντολή χρησιμοποιούμε για να κλείσουμε το Pygame;",
        "options": ["A. pygame.close()", "B. quit()", "C. pygame.quit()", "D. exit()"],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Πώς εμφανίζουμε αλλαγές στην οθόνη του Pygame;",
        "options": ["A. pygame.update()", "B. screen.refresh()", "C. pygame.display.flip()", "D. pygame.load()"],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Ποια είναι η βασική λούπα του παιχνιδιού;",
        "options": ["A. for game in loop:", "B. while True:", "C. repeat forever:", "D. if playing:"],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Ποια είναι η προεπιλεγμένη μονάδα χρόνου του Pygame;",
        "options": ["A. FPS", "B. Seconds", "C. Milliseconds", "D. Ticks"],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Ποια εντολή ρυθμίζει τα FPS;",
        "options": ["A. clock.tick()", "B. set_fps()", "C. pygame.fps()", "D. delay()"],
        "answer": "A",
        "difficulty": "easy"
    },
    {
        "question": "Ποια είναι σωστή μορφή tuple για χρώμα RGB στο Pygame;",
        "options": ["A. (255, 255, 255)", "B. [255, 255, 255]", "C. 255-255-255", "D. 'white'"],
        "answer": "A",
        "difficulty": "easy"
    },
    {
        "question": "Πώς φορτώνεις μια εικόνα στο Pygame;",
        "options": ["A. pygame.load.image()", "B. pygame.image.load()", "C. image.load()", "D. pygame.open_image()"],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Τι τύπου μεταβλητή είναι η εικόνα που φορτώνεται;",
        "options": ["A. string", "B. Surface", "C. Image", "D. Pixel"],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Τι τύπο επιστρέφει η pygame.font.Font();",
        "options": ["A. string", "B. font", "C. surface", "D. object"],
        "answer": "D",
        "difficulty": "easy"
    },
    {
        "question": "Ποια συνάρτηση χρησιμοποιούμε για να εμφανίσουμε κείμενο;",
        "options": ["A. print()", "B. draw.text()", "C. font.render()", "D. text.show()"],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Πώς τοποθετούμε ένα αντικείμενο στην οθόνη;",
        "options": ["A. screen.blit(obj, position)", "B. draw(obj, position)", "C. screen.show(obj)", "D. object.place()"],
        "answer": "A",
        "difficulty": "easy"
    },
    {
        "question": "Πώς κάνουμε τον παίκτη να κινείται δεξιά;",
        "options": ["A. x += ταχύτητα", "B. y += ταχύτητα", "C. x -= ταχύτητα", "D. y -= ταχύτητα"],
        "answer": "A",
        "difficulty": "easy"
    },
    {
        "question": "Πώς ελέγχουμε αν πατήθηκε το δεξί βελάκι;",
        "options": ["A. keys[RIGHT]", "B. event.key == pg.K_RIGHT", "C. keys['right']", "D. event.key == 'right'"],
        "answer": "B",
        "difficulty": "easy"
    },

    {
        "question": "Ποια μέθοδος χρησιμοποιείται για να περιστρέψουμε μια εικόνα στο Pygame;",
        "options": ["A. pygame.transform.rotate()", "B. pygame.image.rotate()", "C. pygame.rotate()", "D. pygame.transform.turn()"],
        "answer": "A",
        "difficulty": "medium"
    },
    {
        "question": "Πώς μπορούμε να ανιχνεύσουμε σύγκρουση μεταξύ δύο ορθογωνίων στο Pygame;",
        "options": ["A. rect.collide(rect2)", "B. pygame.rect.colliderect()", "C. rect.colliderect(rect2)", "D. pygame.collision(rect, rect2)"],
        "answer": "C",
        "difficulty": "medium"
    },
    {
        "question": "Ποια μέθοδος επιστρέφει όλα τα συμβάντα (events) από την ουρά του Pygame;",
        "options": ["A. pygame.event.get()", "B. pygame.get.events()", "C. pygame.event.poll()", "D. pygame.event.all()"],
        "answer": "A",
        "difficulty": "medium"
    },
    {
        "question": "Ποια είναι η σωστή σύνταξη για να διαβάσουμε ένα αρχείο κειμένου στη Python;",
        "options": [
            "A. open('file.txt', 'r')", 
            "B. read('file.txt')", 
            "C. file.open('file.txt')", 
            "D. open('file.txt', 'w')"
        ],
        "answer": "A",
        "difficulty": "medium"
    },
    {
        "question": "Ποια εντολή εμφανίζει το μήκος μιας λίστας mylist στη Python;",
        "options": [
            "A. mylist.length()", 
            "B. len(mylist)", 
            "C. length(mylist)", 
            "D. mylist.len()"
        ],
        "answer": "B",
        "difficulty": "medium"
    },
    {
        "question": "Πώς δηλώνουμε μια συνάρτηση στη Python;",
        "options": [
            "A. function myfunc():", 
            "B. def myfunc():", 
            "C. func myfunc():", 
            "D. define myfunc():"
        ],
        "answer": "B",
        "difficulty": "medium"
    },
    {
        "question": "Ποια είναι η σωστή σύνταξη για λίστα με τους αριθμούς 1, 2, 3 στη Python;",
        "options": [
            "A. (1,2,3)", 
            "B. [1,2,3]", 
            "C. {1,2,3}", 
            "D. <1,2,3>"
        ],
        "answer": "B",
        "difficulty": "medium"
    },
    {
        "question": "Πώς ελέγχουμε αν το x είναι μεγαλύτερο από 10 στη Python;",
        "options": [
            "A. if x > 10:", 
            "B. if x => 10:", 
            "C. if (x > 10)", 
            "D. if x gt 10:"
        ],
        "answer": "A",
        "difficulty": "medium"
    },

    {
        "question": "Πώς μπορούμε να δημιουργήσουμε ένα custom event στο Pygame;",
        "options": [
            "A. pygame.event.Event()", 
            "B. pygame.create_event()", 
            "C. pygame.event.custom()", 
            "D. pygame.event.make()"
        ],
        "answer": "A",
        "difficulty": "hard"
    },
    {
        "question": "Ποια είναι η σωστή διαδικασία για να φορτώσουμε και να παίξουμε έναν ήχο στο Pygame;",
        "options": [
            "A. pygame.mixer.Sound('sound.wav').play()", 
            "B. pygame.sound.play('sound.wav')", 
            "C. pygame.audio.play('sound.wav')", 
            "D. pygame.mixer.play('sound.wav')"
        ],
        "answer": "A",
        "difficulty": "hard"
    }
]


easy_qs = [q for q in questions if q.get("difficulty") == "easy"]
medium_qs = [q for q in questions if q.get("difficulty") == "medium"]

selected_quiz = []
selected_quiz += random.sample(easy_qs, 3)
selected_quiz += random.sample(medium_qs, 3)
random.shuffle(selected_quiz)
quiz = selected_quiz

score = 0
current_q = 0
user_name = ""
start_time = 0
elapsed_time = 0

def format_time(secs):
    mins = int(secs // 60)
    sec = int(secs % 60)
    return f"{mins:02d}:{sec:02d}"

def get_points(q):
    if q.get("difficulty") == "easy":
        return 1
    elif q.get("difficulty") == "medium":
        return 2
    elif q.get("difficulty") == "hard":
        return 3
    return 0

def save_score(name, score, elapsed_time):
    with open("top_scores.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}: {score} βαθμοί, Χρόνος: {format_time(elapsed_time)}\n")

def read_leaderboard():
    try:
        with open("top_scores.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "No scores yet!"

def show_leaderboard():
    leaderboard = read_leaderboard()
    lb_window = tk.Toplevel(root)
    lb_window.title("Leaderboard")
    lb_window.geometry("420x370")
    lb_window.configure(bg="#f7e7ce")
    tk.Label(lb_window, text="🏆 Leaderboard", font=("Arial", 16, "bold"), bg="#f7e7ce", fg="#b8860b").pack(pady=10)
    frame = tk.Frame(lb_window, bg="#fff8dc", bd=2, relief="groove")
    frame.pack(padx=10, pady=5, fill="both", expand=True)
    text = tk.Text(frame, width=50, height=15, bg="#fff8dc", fg="#333", font=("Consolas", 11))
    text.pack()
    text.insert(tk.END, leaderboard)
    text.config(state=tk.DISABLED)

def update_timer():
    global start_time, timer_label
    if start_time > 0:
        now = time.time()
        elapsed = now - start_time
        timer_label.config(text=f"⏰ Χρόνος: {format_time(elapsed)}")
        timer_label.after(500, update_timer)

def next_question():
    global current_q, score
    if current_q > 0:
        selected = answer_var.get()
        if not selected:
            messagebox.showwarning("Προσοχή", "Επίλεξε μια απάντηση!")
            return
        q_prev = quiz[current_q-1]
        if selected == q_prev["answer"]:
            points = get_points(q_prev)
            score += points
            feedback_label.config(
                text=f"✅ Σωστά! (+{points} βαθμοί)", fg="#228B22", bg="#eaffea"
            )
        else:
            feedback_label.config(
                text=f"❌ Λάθος! Η σωστή απάντηση ήταν: {q_prev['answer']}", fg="#b22222", bg="#ffeaea"
            )
    else:
        feedback_label.config(text="", bg=main_bg)

    if current_q < len(quiz):
        q = quiz[current_q]
        diff = q.get("difficulty", "easy")
        diff_str = {"easy": "Εύκολη", "medium": "Μέτρια", "hard": "Δύσκολη"}.get(diff, "")
        question_label.config(
            text=f"({diff_str}) Ερώτηση {current_q+1}: {q['question']}"
        )
        for i, opt in enumerate(q["options"]):
            option_buttons[i].config(text=opt, value=opt[0], bg="#f0f8ff", activebackground="#e6e6fa")
        answer_var.set("")
        current_q += 1
    else:
        finish_quiz()

def finish_quiz():
    global elapsed_time
    for btn in option_buttons:
        btn.pack_forget()
    next_btn.pack_forget()
    feedback_label.config(text="", bg=main_bg)
    elapsed_time = time.time() - start_time
    timer_label.config(text=f"⏰ Τελικός Χρόνος: {format_time(elapsed_time)}")
    result = f"🎯 Βαθμολογία: {score} βαθμοί\nΧρόνος: {format_time(elapsed_time)}"
    if score >= 10:
        result += "\n🏆 Τέλειο! Είσαι master στο Pygame!"
        result_emoji = "🌟"
        color = "#228B22"
    elif score >= 6:
        result += "\n👏 Μπράβο! Τα πας πολύ καλά!"
        result_emoji = "👍"
        color = "#1e90ff"
    else:
        result += "\n🔁 Συνέχισε να προπονείσαι! Θα τα πας καλύτερα την επόμενη φορά!"
        result_emoji = "💡"
        color = "#b22222"
    question_label.config(text=result_emoji + "\n" + result, fg=color, bg="#fffbe7")
    save_score(user_name, score, elapsed_time)
    leaderboard_btn.pack(pady=10)

def start_game():
    global user_name, start_time
    user_name = simpledialog.askstring("Όνομα", "Πώς σε λένε;")
    if not user_name:
        root.destroy()
        return
    welcome_frame.pack_forget()
    question_frame.pack(pady=10, fill="both", expand=True)
    for btn in option_buttons:
        btn.pack(anchor="w", padx=40, pady=2)
    next_btn.pack(pady=10)
    feedback_label.pack(pady=5)
    timer_label.pack(pady=5)
    start_time = time.time()
    update_timer()
    next_question()

main_bg = "#e0f7fa"
root = tk.Tk()
root.title("Python + Pygame Quiz Show")
root.geometry("600x500")
root.configure(bg=main_bg)

# Welcome Frame with color and emoji
welcome_frame = tk.Frame(root, bg="#f7cac9", bd=4, relief="ridge")
welcome_frame.pack(pady=40, padx=40, fill="both", expand=True)
tk.Label(
    welcome_frame,
    text="🎮 Καλωσόρισες στο\nPython + Pygame Quiz Show!",
    font=("Arial Rounded MT Bold", 18, "bold"),
    bg="#f7cac9",
    fg="#4b2e83"
).pack(pady=20)
tk.Label(
    welcome_frame,
    text="Απάντησε σε 5 τυχαίες ερωτήσεις!",
    font=("Comic Sans MS", 13),
    bg="#f7cac9",
    fg="#4b2e83"
).pack(pady=10)
start_btn = tk.Button(
    welcome_frame,
    text="🚀 Έναρξη",
    font=("Arial", 14, "bold"),
    bg="#4b2e83",
    fg="#fff",
    activebackground="#b39ddb",
    activeforeground="#fff",
    width=12,
    command=start_game
)
start_btn.pack(pady=20)

# Quiz Frame
question_frame = tk.Frame(root, bg="#fffbe7", bd=3, relief="groove")
question_label = tk.Label(
    question_frame,
    text="",
    font=("Arial", 14, "bold"),
    wraplength=550,
    justify="left",
    bg="#fffbe7",
    fg="#4b2e83"
)
question_label.pack(pady=10)
timer_label = tk.Label(
    question_frame,
    text="⏰ Χρόνος: 00:00",
    font=("Arial", 12, "bold"),
    bg="#fffbe7",
    fg="#b22222"
)
answer_var = tk.StringVar()
option_buttons = [
    tk.Radiobutton(
        question_frame,
        text="",
        variable=answer_var,
        value="",
        font=("Arial", 12),
        bg="#f0f8ff",
        fg="#222",
        selectcolor="#b3e5fc",
        activebackground="#e6e6fa"
    ) for _ in range(4)
]
next_btn = tk.Button(
    question_frame,
    text="Επόμενη ➡️",
    font=("Arial", 12, "bold"),
    bg="#4b2e83",
    fg="#fff",
    activebackground="#b39ddb",
    activeforeground="#fff",
    width=12,
    command=next_question
)
feedback_label = tk.Label(
    question_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg="#fffbe7"
)

leaderboard_btn = tk.Button(
    question_frame,
    text="Δες Leaderboard 🏅",
    font=("Arial", 13, "bold"),
    bg="#ffd700",
    fg="#4b2e83",
    activebackground="#fff176",
    activeforeground="#4b2e83",
    command=show_leaderboard
)

root.mainloop()
