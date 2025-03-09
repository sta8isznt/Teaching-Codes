class Node:
    def __init__(self, key):
        self.key = key
        self.children = [] # List of Nodes

def new_node(key):
    return Node(key)

# Function to find tree height
def height(root):
    # Base Case
    if root == None:
        return -1
    
    h = -1
    for child in root.children:
        h = max(h, height(child))
    return h+1 # Calculate the current node in the height

def search_tree(root, value):
    """Search if the value exists in the tree. If it exists return this Node"""
    # Base case
    if root == None:
        return None
    
    # Check if the root key is the value
    if root.key == value:
        return root
    
    for child in root.children:
        node = search_tree(child, value)
        if node.key == value:
            return node


if __name__ == "__main__":
    # Create a tree
    root = new_node(1)
    root.children.append(new_node(2))
    root.children.append(new_node(3))
    root.children[0].children.append(new_node(4))
    root.children[0].children.append(new_node(5))
    root.children[1].children.append(new_node(6))
    root.children[1].children.append(new_node(7))
    root.children[0].children[0].children.append(new_node(8))

    # Test the height function
    print("Height of the tree is:", height(root))

    # Test the search_tree function
    search_result = search_tree(root, 5)
    if search_result:
        print(f"Node with key 5 found: {search_result.key}")
    else:
        print("Node with key 5 not found")

    search_result = search_tree(root, 10)
    if search_result:
        print(f"Node with key 10 found: {search_result.key}")
    else:
        print("Node with key 10 not found")