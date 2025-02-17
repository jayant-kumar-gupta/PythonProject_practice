'''
Understanding Inheritance in Python
Inheritance is one of the core concepts in Object-Oriented Programming (OOP).
It allows a class to inherit attributes and methods from another class.
In simpler terms, inheritance is like a child class inheriting traits (methods and properties) from a parent class.
This promotes code reuse and makes your programs more modular and easier to maintain.

Key Concepts:
1. Parent Class (or Base Class): The class whose attributes and methods are inherited.
2. Child Class (or Subclass): The class that inherits the attributes and methods from the parent class.
3. Method Overriding: The ability of the child class to provide a specific implementation of a
method that is already defined in the parent class.
'''

'''
How Inheritance Works in Python:
The child class automatically inherits all methods and attributes of the parent class, but 
it can also add its own methods or override the ones inherited from the parent.
A child class can call methods from the parent class using the super() function.
'''

# Parent class
class Animal:
    # Constructor (initializer)
    def __init__(self, name):
        self.name = name  # Attribute of the parent class

    # Method of the parent class
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class
class Dog(Animal):
    # Constructor of the child class
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the parent class constructor
        self.breed = breed  # Adding a new attribute for the child class

    # Method overriding: The child class defines its own version of speak
    def speak(self):
        print(f"{self.name} barks")

# Child class
class Cat(Animal):
    # Constructor of the child class
    def __init__(self, name, color):
        super().__init__(name)  # Calling the parent class constructor
        self.color = color  # Adding a new attribute for the child class

# Create instances of the child classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "White")

# Calling methods
dog.speak()  # This will call the Dog's speak method
cat.speak()  # This will call the Cat's speak method

'''
Explanation:
1. Parent Class (Animal): Animal has an attribute name and a method speak.
    speak() is a general method that could be used by any animal, but it is a basic implementation.

2. Child Class (Dog): Dog inherits from Animal. 
    It has its own constructor that calls the parent constructor using super().__init__(name).
    Dog overrides the speak() method to provide a more specific behavior (it barks).
    
3. Child Class (Cat): Cat also inherits from Animal and has its own constructor and speak() method. 
    In this case, the speak() method makes the cat meow.
    
Creating Objects:We create instances of the Dog and Cat classes, and then we call their speak() methods.
'''