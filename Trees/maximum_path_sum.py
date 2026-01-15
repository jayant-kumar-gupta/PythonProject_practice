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
node7 = Node(7)
node8 = Node(8)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node5.left = node7
node5.right = node8

result = 0

def dfs(root: Node):
    global result

    if not root:
        return 0
    
    left = dfs(root.left)
    right = dfs(root.right)

    result = max(result, left + right + root.data)

    return root.data + max(left, right, 0)

dfs(node1)
print(result)