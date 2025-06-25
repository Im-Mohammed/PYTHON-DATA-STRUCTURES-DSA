from LinkedList.sll import *
class Stack:
    def __init__(self):
        self.obj=sll() 
        self.item_count=0
    def is_empty(self):
        return self.obj.is_empty()
    def push(self,value):
        self.obj.insertion_at_top(value)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.obj.delete_first()
            self.item_count-=1
    def peek(self):
        if not self.is_empty():
           return self.obj.start.item
    def size(self):
        return self.item_count
    
myl=Stack()
myl.push(10)
myl.push(20)
myl.push(30)
myl.pop()
myl.pop()
print(myl.peek())
print(myl.size())