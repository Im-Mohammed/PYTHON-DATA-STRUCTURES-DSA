from sll import *
class Queue:
    def __init__(self,rear=None):
        self.obj=sll()
        self.rear=rear
        self.item_count=0
    def is_empty(self):
        return self.obj.is_empty()
    def enqueue(self,value):
        self.rear=self.obj.insert_at_last(value)
        self.item_count+=1
    def dequeue(self):
        if not self.is_empty():
            self.obj.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Queue is empty")
    def get_front(self):
        return self.obj.start.item
    def get_rear(self):
        return self.rear.item
    def size(self):
        return self.item_count
qu=Queue()
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
qu.enqueue(50)
print(qu.get_rear())
print(qu.get_front())
print(qu.is_empty())
qu.dequeue()
print(qu.get_front())
print(qu.get_rear())
print(qu.size())