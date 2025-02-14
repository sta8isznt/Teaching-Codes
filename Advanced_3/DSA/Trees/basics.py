class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

# Δημιουργία κόμβου
def new_node(new_key):
    return Node(new_key)

# Ύψος δέντρου
def height(root):
    if root is None:
        return -1
    h = -1
    for child in root.children:
        h = max(h, height(child))
    return h + 1

# Αναζήτηση κόμβου -> Επιστρέφει τον κόμβο με κλειδί k ή None
def search_tree(root, k):
    if root is not None:
        if root.key == k:
            return root
        for child in root.children:
            found = search_tree(child, k)
            if found is not None:
                return found
    return None
