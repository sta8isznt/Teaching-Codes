my_dict = {'Eua': [15, 20],
         'Panos' : 17,
         'Anna': 50}

# Αν θέλουμε να εκτυπώσουμε στον χρήστη την τιμή κάποιου κλειδιού που βρίσκεται μέσα στο
# λεξικό μας κάνουμε παρόμοια διαδικασία με αυτήν στις λίστες

print(my_dict["Panos"])
print(my_dict.get("Andreas", "You have no such friend"))
# print(my_dict["Adreas"])

# Ποιό είναι το πρόβλημα με αυτό?
# Αν δεν υπάρχει το κλειδί που ψάχνουμε μέσα στο λεξικό μας, η Python μας επιστρέφει
# μήνυμα λάθους!

# Καλύτερος τρόπος προσπέλασης: get()
# To get() είναι μία συνάρτηση που μας δίνει την δυνατότητα αν το κλειδί που ψάχνουμε 
# στο λεξικό μας δεν υπάρχει, αντί για μήνυμα λάθους, να παίρνουμε ένα user-friendly μήνυμα!

my_dict["Anna"] = 16
print(my_dict.get("Anna"))

my_dict["Adreas"] = 30
print(my_dict)

# Μπορούμε να εκτυπώσουμε και ολόκληρο το λεξικό μας αν απλά βάλουμε μέσα σε ένα print το όνομά του

# Πώς μπορώ να αλλάξω την τιμή ενός κλειδιού στο λεξικό?

# Παρατήρηση: Αν το κλειδί που πάω να αλλάξω δεν υπάρχει θα προστεθεί στο λεξικό!

value = my_dict.pop("Panos")
print(value + 1)

my_dict = {'Eua': [15, 20],
         'Panos' : 17,
         'Anna': 50}

for name, num in my_dict.items():
    print(f"{name} fav num is {num}")