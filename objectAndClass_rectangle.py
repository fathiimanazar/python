class Rectangle:
    def __init__(self):
        self.length = int(input("Enter the lenght:"))
        self.breadth  = int(input("Enter the breadth:"))

    def area(self):
        return self.length*self.breadth
    def peri(self):
        return 2*(self.length+self.breadth)
R=Rectangle()
print("AREA=",R.area())
print("PERIMETER=",R.peri())

