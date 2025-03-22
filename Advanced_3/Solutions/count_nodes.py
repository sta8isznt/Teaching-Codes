class TreeNode:
    def __init__(self, key):
        self.key = key
        self.children = []


def count_nodes(root):
    """Return the total number of nodes in this tree"""
    # Base case
    if root == None:
        return 0
    
    counter = 1
    for child in root.children:
        counter += count_nodes(child)
    return counter

def max_node(root):
    """Returns the maximum key of the tree"""