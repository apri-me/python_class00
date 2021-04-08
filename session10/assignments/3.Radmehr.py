class Triangle:
    def __init__(self, side1 , side2 , base , height ,color ):
        self.side1 = side1
        self.side2 = side2
        self.base = base
        self.height = height
        self.color = color

    def area (self):
       return    (self.base * self.height)/2

    def surrounding(self):
        return   self.side1 + self.side2 + self.base

      

triangle1 = Triangle ( 3 , 4 , 6 , 2 , 'pink' )



triangle2 = Triangle (6 , 8 , 10 , 12 , 'White' )


print('side1,side2,base,height,color,area and surrounding of triangle1 :')
print( triangle1.side1)
print( triangle1.side2)
print( triangle1.base)
print( triangle1.height)
print( triangle1.color)
print( triangle1.area())
print( triangle1.surrounding())
print()
print('side1,side2,base,height,color,area and surrounding of triangle2 :')
print( triangle2.side1)
print( triangle2.side2)
print( triangle2.base)
print( triangle2.height)
print( triangle2.color)
print( triangle2.area())
print( triangle2.surrounding())