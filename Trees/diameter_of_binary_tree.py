class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

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

result = 0

def diameter(root: Node):
    global result
    
    if not root:
        return -1
    
    left = diameter(root.left)
    right = diameter(root.right)

    result = max(result, 2 + left + right)

    return 1 + max(left,right)

diameter(node1)
print(result)