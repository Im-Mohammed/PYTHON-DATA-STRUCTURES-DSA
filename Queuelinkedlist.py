class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.item_count=0
    def is_empty(self):
        return self.front is None
    def enqueue(self,value):
        if not self.is_empty():
            n=Node(value)
            self.rear.next=n
            self.rear=n
            self.item_count+=1
        else:
            n=Node(value,None)
            self.front=n
            self.rear=n
            self.item_count=1
    def dequeue(self):
        if not self.is_empty():
            self.front=self.front.next
        else:
            raise IndexError("Queue is empty")
    def get_front(self):
        return self.front.item
    def get_rear(self):
        return self.rear.item
    def size(self):
        return self.item_count
    
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