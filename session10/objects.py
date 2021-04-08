class Rectangle:
    def __init__(self, side1 , side2):
        self.side1 = side1
        self.side2 = side2

    
    def __len__(self):
        return self.side1 + self.side2


    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    
    def __str__(self):
        return "Rectangle: ({}, {})".format(self.side1, self.side2)

    # def __delattr__(self, name):
    #     return super().__delattr__(name)

    def area (self):
       return   self.side1 * self.side2

    def surrounding(self):
        return  (self.side1 * 2) + (self.side2 * 2)


class Square(Rectangle):
    def __init__(self, side):
        self.side1 = side
        self.side2 = side



# s1 = Square(3)

# print(len(s1))

# del s1

# print(s1)


r1 = Rectangle(3, 6)
r2 = Square(4)

print( r1 == r2 )

print(r1)

del r1.side1

print(r1)