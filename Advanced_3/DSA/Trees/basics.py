class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

# Δημιουργία κόμβου
def new_node(new_key):
    return Node(new_key)

# Ύψος δέντρου
def height(root):
    if root is None: # base case
        return -1
    h = -1
    for child in root.children:
        h = max(h, height(child))
    return h + 1 # calculate the current node in the height

# Αναζήτηση κόμβου -> Επιστρέφει τον κόμβο με κλειδί k ή None
def search_tree(root, k):
    if root is None: # base case (think about the children of the leaves)
        return None
    if root.key == k: # We found it!
        return root
    for child in root.children: # Do the same process for the childrem of the current Node
        found = search_tree(child, k)
        if found is not None:
            return found
