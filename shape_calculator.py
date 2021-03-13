class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):       
        return (self.__class__.__name__
            + f'(width={self.width}'
            + f', height={self.height})')
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):

        if (self.width > 50) or (self.height > 50):
            return "Too big for picture."
        else:
            return ('*' * self.width + '\n') * self.height
    
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)
    
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        # super().__init__(self.width, self.height)

    def __str__(self):       
        return (self.__class__.__name__
            + f'(side={self.width})')

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.set_side(width)
    
    def set_height(self, height):
        self.set_side(height)

# SCRATCH

# char = '*'
# up_down_pattern = char
# middle_pattern = char + ' '*(self.width-2) + char + '\n'

## contour pattern

# picture = (             
#     up_down_pattern * self.width + '\n'
#     + middle_pattern * (self.height-2)
#     + up_down_pattern * self.width
# )