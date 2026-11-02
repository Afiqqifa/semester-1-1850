# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from point import Point
from shapes import Shape

class Circle(Shape):
    def __init__(self,radius,position,colour):
        super().__init__(position,colour)
        self.set_radius(radius)
    
    def set_radius(self,radius):
        if not isinstance(radius,(int,float)):
            raise TypeError("radius must be a number")
        if radius<=0:
            raise ValueError("radius must be positive")
        self.radius=radius
    
    def area(self):
        areacircle=(self.radius**2)*3.14
        return areacircle
    
    def perimeter(self):
        perimeter=2*3.14*self.radius
        return perimeter
    
    def __str__(self):
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

p1=Point(1,1)
c1=Circle(5,p1,"red")
print(c1)
print("Area:",f"{c1.area():.2f}")
print("Perimeter:",f"{c1.perimeter():.2f}")