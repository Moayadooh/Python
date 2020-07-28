class Shape:
    width = 0
    height = 0

    def area(self):
        print("Parent class area")


class Rectangle:
    def __init__(self,w,h):
        self.width = w  # use parent class variables
        self.height = h

    def area(self):
        print("Rectangle area is :",self.width*self.height)  # override parent class function


class Triangle:
    def __init__(self,w,h):
        self.width = w
        self.height = h

    def area(self):
        print("Triangle area is :",(self.width*self.height)/2)


rectangle = Rectangle(2,4)
rectangle.area()

triangle = Triangle(2,4)
triangle.area()



class Print:
    def Name(self,name=None):
        if name is not None:
            print("your name is",name)
        else:
            print("no name")

PrintName = Print()
PrintName.Name("Moayad")
