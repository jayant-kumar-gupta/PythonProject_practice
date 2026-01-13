import collections
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

def right_view(root: Node):
    result = []
    q = collections.deque([root])

    while q:
        rightside = None
        qLen = len(q)

        for _ in range(qLen):
            node = q.popleft()
            rightside = node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        if rightside:
            result.append(rightside.data)
    return result

def left_view(root: Node):
    result = []
    q = collections.deque([root])

    while q:
        leftside = None
        qLen = len(q)

        for _ in range(qLen):
            node = q.popleft()
            leftside = node
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        
        if leftside:
            result.append(leftside.data)
    return result

def top_view(root: Node):
    pass

def bottom_view(root: Node):
    pass


print(right_view(node1))
print(left_view(node1))