class Stack:
    def __init__(self):
        self.array = []
    def push(self, value):
        self.array.append(value)
    def pop(self):
        return self.array.pop()
    def is_empty(self):
        return not self.array

def test_parenthesis(x):
    obj = Stack()
    if not x:
        return "Empty input"
    for character in x:
        if character == '(':
            obj.push('(')
        else:
            if obj.is_empty():
                return "Not balanced"
            print("An item removed. i.e. ",obj.pop())
    if obj.is_empty():
        return "Balanced"
    else:
        return "Not balanced"

test = input("Enter parenthesis (small) combinations: ")
print(test_parenthesis(test))