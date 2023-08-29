class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self): 
        return 'Rectangle(width={}, height={})'.format(self.width,self.height)
        
    def set_width(self,new_width):
        self.width = new_width
        
    def set_height(self,new_height):
        self.height = new_height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height **2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ''
        for x in range(0,self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self,shape):
        amount_inside = 0
        big_area = self.get_area()
        small_area = shape.get_area()
        while shape.width <= self.width and shape.height <= self.height and big_area >= small_area:
            amount_inside += 1
            big_area -= small_area
        return amount_inside


class Square(Rectangle):
    
    def __init__(self,side):
        Rectangle.__init__(self,side,side)
        self.side = side

    def __str__(self): 
        return 'Square(side={})'.format(self.side)

    def set_side(self,new_side):
        Rectangle.set_height(self, new_side)
        Rectangle.set_width(self, new_side)
        self.side = new_side

    def set_width(self,new_side):
        Rectangle.set_height(self, new_side)
        Rectangle.set_width(self, new_side)
        self.side = new_side

    def set_height(self, new_side):
        Rectangle.set_height(self, new_side)
        Rectangle.set_width(self, new_side)
        self.side = new_side