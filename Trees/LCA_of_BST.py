class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

node5 = Node(5)
node4 = Node(4)
node9 = Node(9)
node3 = Node(3)
node7 = Node(7)
node6 = Node(6)
node8 = Node(8)
node11 = Node(11)
node12 = Node(12)

node5.left = node4
node5.right = node9
node4.left = node3
node9.left = node7
node9.right = node11
node7.left = node6
node7.right = node8
node11.right = node12


def LCA(root, p, q):
    if not root:
        return None
    
    if root.data == p or root.data == q:
        return root
    
    if root.data < p and root.data < q:
        return LCA(root.right, p, q)
    elif root.data > p and root.data > q:
        return LCA(root.left, p, q)
    else:
        return root

print(LCA(node5, 8, 12).data)