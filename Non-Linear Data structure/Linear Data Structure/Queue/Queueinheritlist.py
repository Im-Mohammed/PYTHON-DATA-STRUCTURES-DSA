class Queue(list):
    def is_empty(self):
        return len(self)==0
    def enqueue(self,value):
        self.append(value)
    def dequeue(self):
        if not self.is_empty():
            self.pop(0)
        else:
            raise IndexError("The queue is empty")
    def get_front(self):
        return self[0]
    def get_rear(self):
        return self[-1]
    def size(self):
        return len(self)
    def insert(self,index,value):
        raise AttributeError("Queue has no attribute insert")
obj=Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
print(obj.get_front())
print(obj.get_rear())
print(obj.is_empty())
obj.dequeue()
print(obj.get_front())
print(obj.get_rear())
print(obj.size())
