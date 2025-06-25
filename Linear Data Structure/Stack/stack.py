class stack:
    def __init__(self):
        self.s=[]
    def is_empty(self):
        return self.s==None
    def push(self,value):
        self.s.append(value)
    def pop(self):
        if not self.is_empty():
            return self.s.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.s[-1]
        else:
            raise Exception("Stack is empty ")
    def size(self):
        return len(self.s)

s=stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element is : ",s.peek())
print("removed element is : ",s.pop())
print(s.peek())
print("THe stack size is : ", s.size())