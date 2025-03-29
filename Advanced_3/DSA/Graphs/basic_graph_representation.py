class SymmetricGraph:
    def __init__(self):
        self.adj = {}  # Απλό λεξικό για την αναπαράσταση των γειτονικών λιστών

    def add_edge(self, f, t):
        if f not in self.adj:
            self.adj[f] = []  # Αν ο κόμβος δεν υπάρχει, δημιουργούμε λίστα
        if t not in self.adj:
            self.adj[t] = []
        
        self.adj[f].append(t)
        self.adj[t].append(f)

    def print_graph(self):
        for vertex, neighbors in self.adj.items():
            print(f"[{vertex}]", " -> ".join(map(str, neighbors)))

# Παράδειγμα χρήσης
graph = SymmetricGraph()
edges = [(1, 2), (1, 3), (3, 2), (3, 4), (3, 5), (4, 6)]

for f, t in edges:
    graph.add_edge(f, t)

graph.print_graph()


class WeightedDirectedGraph:
    def __init__(self):
        self.adj = {}  # Απλό λεξικό για αποθήκευση των γειτόνων κάθε κόμβου

    def add_edge(self, f, t, c):
        """Προσθέτει ακμή από τον κόμβο f στον κόμβο t με βάρος c."""
        if f not in self.adj:
            self.adj[f] = []  # Αν ο κόμβος δεν υπάρχει, δημιουργούμε μια κενή λίστα
        self.adj[f].append((t, c))  # Προσθήκη του γείτονα με το βάρος

    def size(self):
        """Επιστρέφει τον αριθμό των κόμβων με τουλάχιστον μία εξερχόμενη ακμή."""
        return len(self.adj)

    def neighbours(self, node):
        """Επιστρέφει τη λίστα γειτόνων του κόμβου node."""
        return self.adj.get(node, [])  # Αν δεν υπάρχει ο κόμβος, επιστρέφουμε κενή λίστα

    def print_graph(self):
        """Εκτυπώνει τον γράφο σε μορφή `[κόμβος] -> γείτονας (βάρος)`."""
        for node, edges in self.adj.items():
            print(f"[{node}]", end="")
            for neighbor, weight in edges:
                print(f" -> {neighbor} ({weight})", end="")
            print()  # Νέα γραμμή για τον επόμενο κόμβο


# Δημιουργία του γράφου και προσθήκη ακμών
graph = WeightedDirectedGraph()

# Προσθήκη ακμών όπως φαίνονται στο διάγραμμα
graph.add_edge(1, 3, 10)
graph.add_edge(1, 5, 15)
graph.add_edge(2, 1, 0)
graph.add_edge(2, 3, 20)
graph.add_edge(2, 4, 30)
graph.add_edge(2, 4, 40)
graph.add_edge(3, 4, 5)
graph.add_edge(3, 5, 35)
graph.add_edge(4, 6, 45)
graph.add_edge(5, 6, 25)

# Εκτύπωση του γράφου
graph.print_graph()
