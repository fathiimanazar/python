class Book:
    def __init__(self):
        self.title = input("Enter the Title:")
        self.author = input("Enter the Author:")
    def display(self):
        if(hasattr(self,'publisher')):
            print(self.title," written by ",self.author," is published by ",self.publisher)
        else:
            print("UNKNOWN PUBLISHER!!")
                
B1=Book()
setattr(B1,'publisher','dc')
B1.display()
