class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
class PriorityQsll:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0
    def push(self,data,prior):
        n=Node(data,prior)
        if not self.start or  prior < self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next != None and temp.next.priority < prior:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1
    def is_empty(self):
        return self.start is None
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        self.start=self.start.next
        self.item_count-=1
    def size(self):
        return self.item_count
    def __iter__(self):
        return PriorityQslliterator(self.start)

class PriorityQslliterator:
    def __init__(self,current):
        self.now=current
    def __iter__(self):
        return self
    def __next__(self):
        if not self.now:
            raise StopIteration
        data=self.now.item
        priority=self.now.priority
        self.now=self.now.next
        return data,priority
    
pq=PriorityQsll()
pq.push(100,6)
pq.push(20,4)
pq.push(30,2)
pq.push(10,1)
pq.push(15,3)
for i in pq:
    print(i)
    