# Finding largest rectangle using python built-in list
def largest_rectangle(heights):
    max_area = 0
    stack  = [] # pair (index,height)
    for i,height in enumerate(heights):
        start = i
        while stack and stack[-1][1]>=height:
            index,length = stack.pop()
            area = length*(i-index)
            max_area = max(area,max_area)
            start = index
        stack.append((start,height))

    for i,height in stack:
        max_area = max(max_area,height * (len(heights)-i))
    return max_area

# print(largest_rectangle([3,2,5,6,2,3]))

#Finding largest rectangle using linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head =new_node
        self.size+=1

    def get_size(self):
        return self.size

    def peek(self):
        return self.head.data if self.head else -1

    def isEmpty(self):
        return True if self.size == 0 else False

    def pop(self):
        if not self.head:
            return None
        if not self.head.next:
            self.size -= 1
            return self.head.data
        removed_value = self.head.data
        self.size -=1
        self.head = self.head.next

        return removed_value
    
def largest_rectangle_ll(array):
    my_stack = Stack()
    max_area = 0

    for i,height in enumerate(array):
        start = i
        while not my_stack.isEmpty() and my_stack.peek()[1]>height:
            index, length = my_stack.pop()
            area = height * (i-index)
            max_area = max(max_area,area)
            start = index
        my_stack.push((start,height))

    while not my_stack.isEmpty():
        i,height = my_stack.pop()
        max_area = max(max_area, height * ( len(array) -i) )
    return max_area
print(largest_rectangle_ll([3,2,5,6,2,3]))