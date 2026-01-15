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

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node7
node3.right = node6

def lca(root: Node, p, q):
    if not root:
        return None
    
    if root == p or root == q:
        return root
    
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    
    return left if left else right

result = lca(node1, node2, node7)
print(result.data)