class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class PriorityQdll:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0
    def push(self,data,priority):
        n=Node(None,(data,priority),None)
        if not self.start or  priority < self.start.item[1]:
            n.next=self.start
            if self.start:
                self.start.prev=n
            self.start=n
        else:   
            temp=self.start
            while temp!=None and temp.item[1] < priority:
                temp=temp.next
            n.next=temp.next
            if temp.next:
                temp.next.prev=n
            temp.next=n
            n.prev=temp
        self.item_count+=1
    def is_empty(self):
        return self.start is None
    def pop(self):
        if not self.is_empty():
            self.start.next.prev=None
            self.start=self.start.next
            self.item_count-=1
        else:
            raise IndexError("PriorityQ underflow")
    def size(slef):
        return slef.item_count
    def __iter__(self):
        return PriorityQdlliterator(self.start)

class PriorityQdlliterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

pq=PriorityQdll()
pq.push(10,8)
pq.push(20,7)
pq.push(30,6)
pq.push(100,1)
pq.push(40,6)
print("The elements of priority queue are: ")
for i in pq:
    print(i)
pq.pop()
pq.pop()
print("After pop() is used: ")
for i in pq:
    print(i)
print(pq.size())
    