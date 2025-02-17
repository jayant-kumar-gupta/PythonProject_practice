class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the perimeter method.")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius
        self.pi = 3.14

    def area(self):
        return round(self.pi * self.radius**2, 2)

    def perimeter(self):
        return round(2 * self.pi * self.radius, 2)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("rectangle")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Main program
def main():
    shape_name = input("Enter the name of the shape (circle/rectangle): ").strip().lower()
    if shape_name == "circle":
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                print("Radius must be a positive number.")
                return
            circle = Circle(radius)
            print(f"Area: {circle.area()} | Perimeter: {circle.perimeter()}")
        except ValueError:
            print("Invalid input! Please enter a numeric value for the radius.")
    elif shape_name == "rectangle":
        try:
            length = float(input("Enter the length of the rectangle: "))
            breadth = float(input("Enter the breadth of the rectangle: "))
            if length <= 0 or breadth <= 0:
                print("Length and breadth must be positive numbers.")
                return
            rectangle = Rectangle(length, breadth)
            print(f"Area: {rectangle.area()} | Perimeter: {rectangle.perimeter()}")
        except ValueError:
            print("Invalid input! Please enter numeric values for length and breadth.")
    else:
        print("Invalid shape name! Please enter either 'circle' or 'rectangle'.")

if __name__ == "__main__":
    main()

