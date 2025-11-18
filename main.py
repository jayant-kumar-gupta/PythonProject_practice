# Stack Operations: push, pop, peek, size, is_empty
# Implementation of stack using arrays
class Stack_array:
    def __repr__(self):
        return str(self.array)
    def __init__(self):
        self.array = []
    def push(self, value):
        self.array.append(value)
    def pop(self):
        return self.array.pop() if self.array else None
    def peek(self):
        return self.array[-1] if self.array else None
    def __len__(self):
        count = 0
        for _ in self.array:
            count+=1
        return count
    def is_empty(self):
        return not self.array

# list1 = Stack_array()
# list1.push(6)
# list1.push("Ram")
# list1.push("@")
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.peek())
# print(len(list1))
# print(list1.is_empty())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_ll:
    def __init__(self):
        self.head = None
    def __repr__(self):
        return "Empty" if not self.head else ' -> '.join(str(x) for x in self.to_list())
    def to_list(self):
        if not self.head:
            return None
        array = []
        currentNode = self.head
        while currentNode:
            array.append(currentNode.data)
            currentNode = currentNode.next
        return array
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if not self.head:
            return "Cannot pop. Linked list is empty"
        a = self.head
        self.head = self.head.next
        return a.data
    def peek(self):
        return self.head.data
    def size(self):
        if not self.head:
            return 0
        count = 0
        currentNode = self.head
        while currentNode:
            count+=1
            currentNode = currentNode.next
        return count
    def is_empty(self):
        return not self.head

# node = Stack_ll()
# node.push(6)
# node.push("Ram")
# node.push("@")
# print(node.pop())
# print(node)