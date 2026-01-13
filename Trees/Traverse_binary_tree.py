from queue import Queue

# Initializing blueprint for binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

# Depth-first Traversal method

# pre-order method
def preorder(CurrentNode):
    if not CurrentNode:
        return
    print(CurrentNode.data, end=" ")
    preorder(CurrentNode.left)
    preorder(CurrentNode.right)

# in-order method
def inorder(CurrentNode):
    if not CurrentNode:
        return
    inorder(CurrentNode.left)
    print(CurrentNode.data, end=" ")
    inorder(CurrentNode.right)

# post-order method
def postorder(CurrentNode):
    if not CurrentNode:
        return
    postorder(CurrentNode.left)
    postorder(CurrentNode.right)
    print(CurrentNode.data, end=" ")

preorder(node1)
print()
inorder(node1)
print()
postorder(node1)
print()

# Traversing trees by level-order
# We can do this by creating a queue

def traverse(root):
    nodes = Queue()
    nodes.put(root)
    while not nodes.empty():
        currentNode = nodes.get()
        if currentNode.left:
            nodes.put(currentNode.left)
        if currentNode.right:
            nodes.put(currentNode.right)
        print(currentNode.data, end= " ")

traverse(node1)