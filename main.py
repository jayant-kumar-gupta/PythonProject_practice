class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(3)
node3 = Node(9)
node4 = Node(7)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1

def findGreatest(head):
    greatest = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data>greatest:
            greatest = currentNode.data
        currentNode = currentNode.next
    return greatest

def travel(head):
    currentNode = head
    while currentNode != None:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("Null")

def delnode(head,nodetodelete):
    currentNode = head

    if head == nodetodelete:
        return head.next
    
    while currentNode and currentNode.next != nodetodelete:
        currentNode = currentNode.next
    
    currentNode.next = currentNode.next.next
    return head

def insertnode(head,nodetoinsert,position):
    newnode = nodetoinsert
    if position == 1: 
        newnode.next = head
        return newnode
    
    currentNode = head
    for _ in  range(position-2):
        currentNode = currentNode.next

    newnode.next = currentNode.next
    currentNode.next = newnode
    return head

def detect_loop(head):
    fast = head
    slow = head
    while fast and fast.next:
        if fast.next is slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False

def reverse_ll(head):
    previous = None
    currentNode = head
    while currentNode:
        nxt = currentNode.next
        currentNode.next = previous
        previous = currentNode
        currentNode = nxt

    return previous
        



# Find greatest node among Linked list
# print("The greatest number among the linked list is: ",findGreatest(node1))

# Travel through Linked list
# print(travel(node1))

# Delete Node
# node1 = delnode(node1,node1)
# print(travel(node1))

# Insert Node
# node1 = insertnode(node1,Node(6),3)
# print(travel(node1))

# Detect cycle in Linked List
# if detect_loop(node1):
#     print("Linked list is cyclomatic")
# else:
#     print("Linked list is  not cyclomatic")

# Reverse Linked List
# node1 = reverse_ll(node1)
# print(travel(node1))