class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def is_empty(self):
        return len(self.stack) == 0
    def pop(self):
        if not self.is_empty():
            return  self.stack.pop()
        return -1
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def is_empty(self):
        return len(self.queue) == 0
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return -1
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
    
class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

    
def dfs(root):
    if root == None:
        return
    s = Stack()
    s.push(root)
    while not s.is_empty():
        temp = s.pop()
        print(temp.key)
        for child in temp.children[::-1]:
            s.push(child)

def bfs(root):
    if not root:
        return
    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        temp = q.dequeue()
        print(temp.key, end=" ")
        for child in temp.children:
            q.enqueue(child)

def create_sample_tree():
    # Creating a sample tree
    #         1
    #       / | \
    #      2  3  4
    #     / \
    #    5   6
    root = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    child3 = Node(4)
    child1.children = [Node(5), Node(6)]
    root.children = [child1, child2, child3]
    return root

if __name__ == "__main__":
    root = create_sample_tree()
    print("DFS Traversal:")
    dfs(root)
    print()
    bfs(root)

