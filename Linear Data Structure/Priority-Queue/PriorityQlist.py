class PriorityQ:
    def __init__(self):
        self.mylist=[]
    def push(self,data,priority):
        index=0
        while index < len(self.mylist) and self.mylist[index][1]<=priority:
            index+=1
        self.mylist.insert(index,(data,priority))
    def is_empty(self):
        return len(self.mylist)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("Priorityq Is empty")
        self.mylist.pop(0)
    def size(slef):
        return len(slef.mylist)
    def __iter__(self):
        return PriorityQlist_iterator(self.mylist)
class PriorityQlist_iterator:
    def __init__(self,mylist_iter):
        self.obj=mylist_iter
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > len(self.obj)-1:
            raise StopIteration
        data=self.obj[self.current]
        self.current+=1
        return data
        
        
        
##Driver Code
pq=PriorityQ()
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