class Square:
    def __init__(self, side ,color ):
        self.side = side
        self.color = color

    def area (self):
       return    self.side ** 2

    def surrounding(self):
        return   self.side*4