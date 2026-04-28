import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width **2 + self.height ** 2)

    def get_picture(self):
        if((self.width) > 50) or (self.height) > 50:
            return 'Too big for picture.'
        picture_line = ''
        for l in range(self.height):
            picture_line += "*".ljust((self.width), '*') + '\n'
        return picture_line

    def get_amount_inside(self, shape):
        if(shape.get_area() > self.get_area()):
            return 0
        
        difference = math.floor((self.get_area() / shape.get_area()))
        return difference

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
        self.length = length

    def set_width(self,length):
        self.width = length
        self.height = length
        self.length = length

    def set_height(self,length):
        self.width = length
        self.height = length
        self.length = length

    def set_side(self, side):
        self.width = side
        self.height = side
        # super().set_height(side)
        self.length = side


    def __str__(self):
        return f"Square(side={self.length})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))