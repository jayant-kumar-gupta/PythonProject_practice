my_list = ["Even" if x % 2 == 0 else "Odd" for x in range(1,21)]
print(my_list)

tuple_list = [(1, 5), (3, 2), (2, 8)]
print(sorted(tuple_list, key=lambda x:x[1], reverse= True))

def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))