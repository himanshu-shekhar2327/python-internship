
import math

class Circle:
    def __init__(self, x, y, radius):
        
        self.x = x
        self.y = y
        self.radius = radius
    
    def get_area(self):
        
        return math.pi * self.radius ** 2
    
    def get_perimeter(self):
        
        return 2 * math.pi * self.radius
    
    def get_circumference(self):
        
        return self.get_perimeter()

# Takng the input from user
inp_x_coord = float(input("Enter the x-coordinate of the circle :"))
inp_y_coord = float(input("Enter the y coordinate of the circle :"))
inp_rad = float(input("Enter the radius of the circle : "))
circle1 = Circle(inp_x_coord,inp_y_coord,inp_rad)
print(f"Circle with center ({circle1.x}, {circle1.y}) and radius {circle1.radius}:")
print(f"Area: {circle1.get_area()}")
print(f"Perimeter (Circumference): {circle1.get_perimeter()}")
