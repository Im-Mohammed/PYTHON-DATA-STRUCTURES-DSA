from LinkedList.sll import *
class Queue(sll):
    def __init__(self, front=None,rear=None):
        super().__init__(front)
        self.rear=rear
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def enqueue(self,value):
        self.rear=self.insert_at_last(value)
        self.item_count+=1
    def dequeue(self):
        if not self.is_empty():
            data=self.start.item
            self.delete_first()
            self.item_count-=1
            return data
        else:
            raise IndexError("Index out of range")
    def get_front(self):
        return self.start.item
    def get_rear(self):
        return self.rear.item
    def size(self):
        return self.item_count

#driver Code
qu=Queue()
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
qu.enqueue(50)
print(qu.get_front())
print(qu.is_empty())
qu.dequeue()
print(qu.get_front())
print(qu.get_rear())
print(qu.size())