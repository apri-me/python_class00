from math import pi

class Circle:
    def __init__(self, radius, color): # constructor
        self.radius = radius
        self.color = color

    def area(self):
        return round(pi * ( self.radius ** 2 ), 3)
    
    def surrounding(self):
        return round(2 * pi * self.radius)
        

circle1 = Circle(4, 'Red')
# circle1.radius = 2
# circle1.radius = 4
circle2 = Circle(5, 'Green')
# circle2.radius = 5
# print(circle1.radius)
# print(circle1.color)
# print(circle2.radius)
# print(circle2.color)

# print(circle1.area())
# print(circle2.surrounding())
# print(circle2.area())

print(Circle.area(circle1))

