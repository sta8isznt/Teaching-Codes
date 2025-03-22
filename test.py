# Binary Tree Traversals
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder(root):
    # Root -> Left -> Right
    if root == None:
        return
    print(root.key)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    # Left -> Root -> Right
    if root == None:
        return
    inorder(root.left)
    print(root.key)
    inorder(root.right)

def postorder(root):
    # Left -> Right -> Root
    if root ==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.key)

def create_sample_tree():
    # Creating a sample binary tree
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

if __name__ == "__main__":
    root = create_sample_tree()
    print("Preorder Traversal:")
    preorder(root)
    print("\nInorder Traversal:")
    inorder(root)
    print("\nPostorder Traversal:")
    postorder(root)