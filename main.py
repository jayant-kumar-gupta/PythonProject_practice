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