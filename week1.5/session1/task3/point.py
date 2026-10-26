# Week 1.5, Session 1: Task 3
import math

class Point():
    """
    A Point in 2D space.
    """
    # Add constructor 
    def __init__(self,x_coordinate,y_coordinate):
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
    # Add distance() method here
    def distance(self):
        return round(math.sqrt(((self.x_coordinate)**2)+((self.y_coordinate)**2)),2)

    # Add distance_to() method here
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
p=Point(5,2)
print(p.distance())