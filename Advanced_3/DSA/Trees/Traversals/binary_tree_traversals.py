class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Preorder Traversal (Root → Left → Right)
def preorder(root):
    if root:
        print(root.value, end=" ")  # Process root
        preorder(root.left)
        preorder(root.right)

# Inorder Traversal (Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")  # Process root
        inorder(root.right)

# Postorder Traversal (Left → Right → Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

# Example Usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Preorder Traversal:")
    preorder(root)  # Output: 1 2 4 5 3 6 7

    print("\nInorder Traversal:")
    inorder(root)  # Output: 4 2 5 1 6 3 7

    print("\nPostorder Traversal:")
    postorder(root)  # Output: 4 5 2 6 7 3 1