class Square:
    def __init__(self, side ,color ):
        self.side = side
        self.color = color

    def area (self):
       return    self.side ** 2

    def surrounding(self):
        return   self.side*4

      

# square1 = Square( 3 , 'Green' )

# #square.side= 2

# square2 = Square(6, 'Yellow')


# print('side,color,area and surrounding of square1 :')
# print( square1.side)
# print( square1.color)
# print( square1.area())
# print( square1.surrounding())
# print()
# print('side,color,area and surrounding of square2 :')
# print( square2.side)
# print( square2.color)
# print( square2.area())
# print( square2.surrounding())

# s1 = Square(4, "RED")

# s1.area()


# Square.area(s1)

