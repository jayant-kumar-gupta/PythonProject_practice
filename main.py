class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def findGreatest(head):
    greatest = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data>greatest:
            greatest = currentNode.data
        currentNode = currentNode.next
    return greatest



print("The greatest number among the linked list is: ",findGreatest(node1))