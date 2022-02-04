class Rectangle:
    def get(self,len,wid):
        self.len=len
        self.wid=wid
class Cuboid(Rectangle):
    def getheight(self,len,wid,ht):
        self.get(len,wid)
        self.ht=ht
    def __le__(self,other):
        return((self.len*self.wid*self.ht)<=(other.len*other.wid*other.ht))

f1=Cuboid()
f2=Cuboid()
f1.getheight(1,3,2)
f2.getheight(2,3,4)
if f1<=f2:
    print("f1 is less than or equal to f2")
else:
    print("f1 is greater than f2")
    
