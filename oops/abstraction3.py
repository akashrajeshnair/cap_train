from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,c):
        self.color = c 

    def get_color(self):
        return self.color
    
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self):
        return self.side*self.side
    
    def get_perimeter(self):
        return self.side*4
    
def missing_number(l):
    n = len(l) + 1
    req = (n*(n+1))/2
    return req - sum(l)
    
    
s = Square("red", 5)
print(s.get_color())
print(s.get_area())
print(s.get_perimeter())
print(missing_number([1,2,3,4,5,7,8,9,10]))