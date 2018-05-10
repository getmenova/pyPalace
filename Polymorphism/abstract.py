from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        return self.side*self.side
    

class Rectangle(Shape):
    width = 5
    length = 10

    def area(self):
        return self.width * self.length

square = Square()
print('Area of square : ',square.area())
rectangle = Rectangle()
print('Area of rectangle: ',rectangle.area())
#shape = Shape()