class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class dll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,value):
        if self.start is None:
            n=Node(None,value,None)
            self.start=n
        elif self.start.next is None:
            n=Node(None,value,self.start)
            self.start=n
        else:
            n=Node(None,value,self.start)
            self.start.prev=n
            self.start=n
    def insert_at_last(self,value):
        if self.start is None:
            n=Node(None,value,None)
            self.start=n
        elif self.start.next is None:
            n=Node(self.start,value,None)
            self.start.next=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            n=Node(temp,value,None)
            temp.next=n
            
    def search(self,value):
        if self.start.item==value:
            return self.start 
        else:
            temp=self.start
            while temp is not None:
                if temp.item == value:
                    return temp
                temp=temp.next
    def insert_after(self,value,temp):
        if self.start is None:
            pass 
        else:
            n=Node(temp,value,temp.next)
            temp.next.prev=n
            temp.next=n
            
    def print_all_elements(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
        return None
    def delete_at_first(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            self.start=self.start.next
            self.start.prev=None
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
    def delete_at_middle_using_search(self,temp):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp.next=temp.next.next
            temp.next.prev=temp
    def delete_at_middle_value(self,value):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == value:
                self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                if temp.next.item==value:
                    temp.next=temp.next.next
                    temp.next.prev=temp
                temp=temp.next
    def __iter__(self):
        return dlliterator(self.start)

class dlliterator:
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
            

mylist=dll()
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.print_all_elements()
mylist.insert_at_last(60)
mylist.print_all_elements()
print("\n")
mylist.insert_after(40,mylist.search(30))
mylist.print_all_elements()
print("\n")
mylist.insert_after(50,mylist.search(40))
mylist.print_all_elements()
print("\n")
mylist.delete_at_first()
mylist.print_all_elements()
print("\n")
mylist.delete_at_last()
mylist.print_all_elements()
print("\n")
mylist.delete_at_middle_value(40)
mylist.print_all_elements()
print("\n")
mylist.insert_after(40,mylist.search(30))
mylist.print_all_elements()
print("\n")
mylist.delete_at_middle_using_search(mylist.search(20))
mylist.print_all_elements()
print('\n')
for x in mylist:
    print(x)