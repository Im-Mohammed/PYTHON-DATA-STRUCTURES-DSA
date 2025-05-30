class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class sll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insertion_at_top(self,value):
        n=Node(value,self.start) # item and next value will be none
        self.start=n
    def insert_at_last(self,value):
        n=Node(value)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            return n
        else:
            self.start=n
            return n
    def search(self,value):
        temp=self.start
        while temp.next is not None:
            if temp.item==value:
                return temp
            temp=temp.next
        return None
    def insert_at_middle(self,temp,value):
        if temp is not None:
            n=Node(value,temp.next)
            temp.next=n
    def printAllValue(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_at_middle(self,temp):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp.next=temp.next.next
    def __iter__(self):
        return slliterator(self.start)
        
class slliterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
        




"""
myList=sll()
myList.insertion_at_top(20)
myList.insertion_at_top(10)
myList.insert_at_last(50)
myList.insert_at_middle(myList.search(20),25)
myList.insert_at_last(90)
myList.printAllValue()
print('\n')
myList.delete_first()
myList.printAllValue()
print('\n')
myList.delete_at_last()
myList.printAllValue()
print("\n")
myList.delete_at_middle(myList.search(20))
myList.printAllValue()
print('\n')
for x in myList:
    print(x)
"""