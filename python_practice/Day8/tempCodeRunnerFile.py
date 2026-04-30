class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        print(f"the area of circle is {3.14*self.radius**2}")

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        print(f"The area of rectangle is {self.length*self.breadth}")

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def area(self):
        print(f"the area of triangle is {0.5*self.base*self.height}")

cricle=Circle(5)
cricle.area()
rect=Rectangle(4,2)
rect.area()
tri=Triangle(8,5)
tri.area()
