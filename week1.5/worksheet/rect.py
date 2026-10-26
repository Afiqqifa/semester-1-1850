# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than 0.")
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Width and height must be numbers.")

        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        return self.width == self.height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    # (See README.md for details of what they should do)

shape1 = Rectangle(5, 5)
print("Is square:", shape1.is_square())
print("Area:", shape1.area())
print("Perimeter:", shape1.perimeter())

shape2 = Rectangle(4, 6)
print("Is square:", shape2.is_square())
print("Area:", shape2.area())
print("Perimeter:", shape2.perimeter())

