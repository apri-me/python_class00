class Rectangle:
    def __init__(self, side1 , side2 ,color ):
        self.side1 = side1
        self.side2 = side2
        self.color = color

    def area (self):
       return    self.side1 * self.side2

    def surrounding(self):
        return   (self.side1 * 2) + (self.side2 * 2)

      

rectangle1 = Rectangle( 3 , 4 , 'Purple' )



rectangle2 = Rectangle(6 , 8 , 'Orange')


print('side1,side2,color,area and surrounding of rectangle1 :')
print( rectangle1.side1)
print( rectangle1.side2)
print( rectangle1.color)
print( rectangle1.area())
print( rectangle1.surrounding())
print()
print('side1,side2,color,area and surrounding of rectangle2 :')
print( rectangle2.side1)
print( rectangle2.side2)
print( rectangle2.color)
print( rectangle2.area())
print( rectangle2.surrounding())