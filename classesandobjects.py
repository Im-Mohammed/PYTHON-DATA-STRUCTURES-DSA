class Person:
    name='ALi'
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def show(self):
        print(self.name)
        print(self.age)

a=Person('rahul',14)
a.show()
class Circle:
    def __init__(self,radius=None):
        self.radius=radius
    def getRadius(self):
        return self.radius
    def setRadius(self,radius):
        self.radius=radius
    def getArea(self):
        return (3.14*self.radius**2)
    def getCircum(self):
        return 2*3.14*self.radius
c=Circle(3)


print(c.getArea(),c.getCircum(),c.getRadius())
###question 3 
class Rectangle:
    def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
    def setDimensions(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def showDimensions(self):
        print(self.length*self.breadth)
    def getDimesions(self,length,breadth):
        return self.breadth*self.length
r=Rectangle(10,5)
r.getDimesions(10,6)
r.showDimensions()
r.setDimensions(10,2)

class Book:
    def __init__(self,bookid,title,price):
        self.bookid=bookid
        self.title=title
        self.price=price
    def showbook(self):
        print(self.bookid,self.price,self.title)
b=Book(107,'ALi the great',1233)
b.showbook()

class Team:
    def __init__(self,name):
        self.name=name
        self.members=[]
    def setInput(self):
        for _ in range(5):
            a=input("ENter the team member name")
            self.members.append(a)
            
    def showmember(self):
        print(self.members)
t=Team('ali')
t.setInput()
t.showmember()