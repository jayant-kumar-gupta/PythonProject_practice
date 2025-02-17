#An example code of Object-Oriented programming for python

#Class: A certain entities which have its own properties and behaviours.
#Object: An entity of its class.
'''For example: Let phone be a class which has properties like Color, Costs, Size, etc and behaviours like
making phone call, playing games, Using web, etc'''

#A sample code

class Phone: #Creation of class

    def make_call(self):  #associating behaviours with it
        print("Phone is making a call")

    def play_game(self):  #'''The parameter 'self' denotes that the function is the behaviour of the class or
                          #   object rather than only a user-defined function.'''
        print("Phone is ready to play games")

    def set_color(self,color): #One more parameter 'color' is for assigning an attribute(property) to the class.
        self.color=color       #Here self.color becomes the property of class

    def set_cost(self,cost):
        self.cost=cost

    def show_color(self):      #Function to show the properties (like color and cost) and behaves like
        return self.color      # behaviour associated with class

    def show_cost(self):
        return self.cost

samsung = Phone()  #Creating an object related to its class.
samsung.play_game() #ordering object to do its behaviour related to its class
samsung.make_call()

samsung.set_color("Silver") #Setting an attribute (color=Silver) to the object and class
samsung.set_cost(154300)
print(samsung.show_color())
print(samsung.show_cost())

''' The below code is for describing __init__ method in OOP

What is __init__?
In Python, the __init__ method is a special method, sometimes called a constructor, 
that is automatically called when an object (an instance of a class) is created. 
It's used to initialize the state of the object (i.e., setting the values of its attributes).

Why do we need __init__?
When you create an instance of a class, Python needs a way to initialize the object with some initial values. 
The __init__ method allows you to set up the object's attributes when the object is created, 
ensuring that every instance of the class starts with a specific state.

Without the __init__ method, you'd have to manually assign values to each attribute of the object after 
it is created, which is less efficient and can lead to errors.


    class Phone:
    def __init__(self, color, cost):
        self.color = color
        self.cost = cost

    def make_call(self):
        print("Phone is making a call")

    def play_game(self):
        print("Phone is ready to play games")

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

# Creating an object of the Phone class and passing arguments to __init__
samsung = Phone("Silver", 154300)  # __init__ is called automatically
samsung.make_call()
samsung.play_game()

print(f"Phone Color: {samsung.show_color()}")
print(f"Phone Cost: {samsung.show_cost()}")
'''
