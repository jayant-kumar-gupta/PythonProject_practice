'''Arrays in Python
An array is a data structure used to store multiple items of the same type together. In Python, arrays are available through the array module or can be implemented using lists, which are more flexible but not strictly type-bound.

1. Why Use Arrays?
    Arrays are faster than lists for large amounts of data when all elements are of the same type.
    They consume less memory compared to lists.
    Best for storing and performing operations on numeric data.
2. How to Create an Array
   To use arrays, you need to import the array module.
   Here's how you can create one:'''

# Syntax: array.array(typecode, [initial_values])
'''arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' means integer type
print(arr)  # Output: array('i', [1, 2, 3, 4, 5])'''

'''
Typecodes specify the type of data:
'i' for integers
'f' for floats
'd' for double-precision floats
'u' for Unicode characters
'''

#Array elements can be accessed using indexing.
#print(arr[0])  # First element: 1
#print(arr[-1])  # Last element: 5

#You can also modify elements:
#arr[1] = 10  # Change the second element
#print(arr)  # Output: array('i', [1, 10, 3, 4, 5])

'''
4. Common Array Operations

a) Adding Elements
Use append() to add a single element.
    arr.append(6)
    print(arr)  # Output: array('i', [1, 10, 3, 4, 5, 6])

Use extend() to add multiple elements.
    arr.extend([7, 8, 9])
    print(arr)  # Output: array('i', [1, 10, 3, 4, 5, 6, 7, 8, 9])


b) Removing Elements
Use remove() to delete a specific element.
    arr.remove(10)
    print(arr)  # Output: array('i', [1, 3, 4, 5, 6, 7, 8, 9])

Use pop() to remove an element at a specific index.
    arr.pop(0)  # Removes the first element
    print(arr)  # Output: array('i', [3, 4, 5, 6, 7, 8, 9])


c) Slicing
You can extract a subset of elements using slicing.
    subset = arr[1:4]
    print(subset)  # Output: array('i', [4, 5, 6])


5. Iterating Over an Array
    for element in arr:
        print(element)


6. Array Methods

Method	Description

append(x)	    Adds an element x to the end of the array.
extend(iter)	Adds elements from an iterable (e.g., list).
insert(i, x)	Inserts x at index i.
remove(x)	    Removes the first occurrence of x.
pop([i])	    Removes and returns the element at index i.
index(x)	    Returns the first index of x.
reverse()	    Reverses the array in place.
count(x)	    Returns the count of occurrences of x.
'''

#Example
import array

# Store daily temperatures in Celsius
temps = array.array('f', [22.5, 24.0, 19.8, 25.3])

# Add a new day's temperature
temps.append(23.1)

# Convert temperatures to Fahrenheit
fahrenheit = array.array('f', [round((temp * 9/5 + 32),2) for temp in temps])

print("Temperatures in Celsius:", temps)
print("Temperatures in Fahrenheit:", fahrenheit)






