class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def dfs_recursive(node):
    if not node:
        return
    
    print(node.value, end=" ")  # Process node
    
    for child in node.children:
        dfs_recursive(child)

