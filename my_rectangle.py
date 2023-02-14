class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return (2*(self.length+self.breadth))
        
    def disp(self):
        print("the length of the rectangle is :",self.length)
        print("the breadth of the rectangle is :",self.breadth)
        print("the area of the rectangle is :",self.area())
        print("the perimeter of the rectangle is :",self.perimeter())