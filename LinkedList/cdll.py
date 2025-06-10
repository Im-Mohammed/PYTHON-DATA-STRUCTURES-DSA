class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class cdll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,value):
        if self.start is None:
            n=Node(None,value,None)
            self.start=n
            n.prev=self.start
            n.next=self.start
        else:
            n=Node(self.start.prev,value,self.start)
            self.start.prev.next=n
            self.start.prev=n
            self.start=n
    def insert_at_last(self,value):
        if not self.is_empty():
            n=Node(self.start.prev,value,self.start)
            self.start.prev.next=n
            self.start.prev=n
        else:
            n=Node(None,value,None)
            self.start=n
            n.prev=self.start
            n.next=self.start
    def search(self,value):
        if not self.is_empty():
            temp=self.start
            while temp.next != self.start:
                if temp.item == value:
                    return temp
                temp=temp.next
            if temp == self.start:
                if temp.item == value:
                    return temp
            return None
    def insert_after(self,value,item):
        if not self.is_empty():
            temp=self.start
        while temp.next != self.start:
            if temp.item == item:
                n=Node(temp,value,temp.next)
                temp.next.prev = n
                temp.next=n
            temp= temp.next
    def print_all_elements(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                print(temp.item,end=" ")
                temp=temp.next
            if temp == self.start.prev:
                print(temp.item)

    def delete_first(self):
        if self.start.next == self.start.prev :
            self.start = None
        else: 
            self.start.next.prev=self.start.prev
            self.start.prev.next= self.start.next
            self.start = self.start.next
    def delete_at_last(self):
        if self.start.next==self.start.prev:
            self.start= None
        else:
            self.start.prev.prev.next=self.start
            self.start.prev=self.start.prev.prev
    def delete_item(self,value):
        if not self.is_empty():
            temp=self.start
            while temp != self.start.prev:
                if temp.item == value:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                temp=temp.next
    def __iter__(self):
        return cdlliterator(self.start)
    
class cdlliterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current== self.start and self.count ==1 :
            raise StopIteration
        else:
            self.count=1
            data =self.current.item
            self.current=self.current.next
        return data
        
mylist=cdll()
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_last(60)
mylist.insert_at_last(70)
mylist.insert_after(40,30)
mylist.insert_after(50,40)
mylist.print_all_elements()
mylist.delete_first()
mylist.print_all_elements()
mylist.delete_at_last()
mylist.print_all_elements()
mylist.delete_item(40)
mylist.print_all_elements()
print('\n')
for x in mylist:
    print(x)
