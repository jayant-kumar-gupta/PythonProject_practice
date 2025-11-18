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
        return not bool(self.array)

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

# Implementation of stack using Linked List
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

# Queue operations: enqueue, dequeue, size, is_empty, peek
# Queue implementation using array
class Queue_array:
    def __init__(self):
        self.array = []
    def __repr__(self):
        return str(self.array)
    def enqueue(self, value):
        self.array.append(value)
    def dequeue(self):
        return "Unable to dequeue. Queue is empty." if not self.array else self.array.remove(self.array[0])
    def peek(self):
        return self.array[0]
    def size(self):
        return len(self.array)
    def is_empty(self):
        return not bool(self.array)

# list1 = Queue_array()
# list1.enqueue(6)
# list1.enqueue("Ram")
# list1.enqueue("@")
# print(list1)
# list1.dequeue()
# print(list1)
# print(list1.peek())
# print(list1.size())
# print(list1.is_empty())

# Queue implementation using Linked list
class Queue_ll:
    def __init__(self):
        self.head = None
        self.last = None
    def __repr__(self):
        return " -> ".join(str(x) for x in self.to_list()) or "Empty"
    def to_list(self):
        if not self.head:
            return None
        array = []
        currentNode = self.head
        while currentNode:
            array.append(currentNode.data)
            currentNode = currentNode.next
        return array
    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.last = new_node
        self.last.next = new_node
        self.last = new_node
    def dequeue(self):
        if not  self.head:
            return None
        removed_value = self.head
        self.head = self.head.next
        return removed_value
    def peek(self):
        return self.head.data if self.head else None
    def size(self):
        count = 0
        currentNode = self.head
        while currentNode:
            count+=1
            currentNode = currentNode.next
        return count
    def is_empty(self):
        return bool(self.head)

list1 = Queue_ll()
list1.enqueue(6)
list1.enqueue("Ram")
list1.enqueue("@")
print(list1)
# list1.dequeue()
# print(list1)
# print(list1.peek())
# print(list1.size())
# print(list1.is_empty())