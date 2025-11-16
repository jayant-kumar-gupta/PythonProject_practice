from itertools import count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(9)
node6 = Node(11)
node7 = Node(13)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7


def findGreatest(head):
    greatest = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data > greatest:
            greatest = currentNode.data
        currentNode = currentNode.next
    return greatest


def travel(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("Null")


def delnode(head, nodetodelete):
    currentNode = head

    if head == nodetodelete:
        return head.next

    while currentNode and currentNode.next != nodetodelete:
        currentNode = currentNode.next

    currentNode.next = currentNode.next.next
    return head


def insertnode(head, nodetoinsert, position):
    newnode = nodetoinsert
    if position == 1:
        newnode.next = head
        return newnode

    currentNode = head
    for _ in range(position - 2):
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


def merge(head1, head2):
    a, b = head1, head2
    if not a:
        return b
    if not b:
        return a

    if a.data <= b.data:
        head = a
        a = a.next
    else:
        head = b
        b = b.next

    currentNode = head
    while a and b:
        if a.data <= b.data:
            currentNode.next = a
            a = a.next
        else:
            currentNode.next = b
            b = b.next
        currentNode = currentNode.next

    if a:
        currentNode.next = a
    else:
        currentNode.next = b

    return head


def kth_from_end(head, k):
    fast = head
    slow = head

    for _ in range(k):
        if not fast:
            return None
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow.data

# Find the greatest node among Linked list
# print("The greatest number among the linked list is:",findGreatest(node1))

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

# Merge two sorted Linked Lists
# node11 = Node(11)
# node12 = Node(13)
# node13 = Node(15)
# node14 = Node(17)
# node15 = Node(19)
#
# node11.next = node12
# node12.next = node13
# node13.next = node14
# node14.next = node15
#
# head_node = merge(node1,node11)
# print(travel(head_node))

# finding Kth element from end
# print(kth_from_end(node1,3))