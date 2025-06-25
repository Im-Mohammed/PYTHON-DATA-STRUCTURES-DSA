class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class csll:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_at_first(self,value):
        if not self.is_empty():
            n=Node(value,self.last.next)
            self.last.next=n
        else:
            n=Node(value)
            self.last=n
            self.last.next=self.last
    def insert_at_last(self,value):
        if not self.is_empty():
            n=Node(value,self.last.next)
            self.last.next=n
            self.last=n
        else:
            self.last=n
    def search(self,value):
        if self.last.item == value:
            return self.last
        else:
            temp=self.last.next
            while temp.next != self.last.next:
                if temp.item ==value:
                    return temp
                temp=temp.next
            return None
    def insert_after(self,value,temp):
        if not self.is_empty():
            n=Node(value,temp.next)
            temp.next=n
    def print_all_elements(self):
        temp=self.last.next
        while temp.next != self.last.next:
            print(temp.item,end=" ")
            temp=temp.next
        if temp == self.last:
            print(temp.item,end=" ")
    def delete_at_first(self):
        if not self.is_empty():
            self.last.next=self.last.next.next
        elif self.last.next.next == self.last:
             self.last.next=self.last
        else:
            self.last=None
    def delete_at_last(self):
        if self.last is None:
            pass
        elif self.last.next == self.last:
            self.last= None
        else:
            temp=self.last.next
            while temp.next != self.last:
                temp=temp.next 
            temp.next=self.last.next
            self.last=temp
    def delete_item(self,value):
        if not self.is_empty():
            temp=self.last.next
            while temp.next != self.last.next:
                if temp.next.item == value:
                    temp.next=temp.next.next
                temp=temp.next
    
mylist=csll()
mylist.insert_at_first(10)
mylist.insert_at_first(5)
mylist.print_all_elements()
print('\n')
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.print_all_elements()
print('\n')
mylist.insert_after(25,mylist.search(20))
mylist.insert_after(15,mylist.search(10))
mylist.print_all_elements()
print('\n')
mylist.delete_at_first()
mylist.print_all_elements()
print('\n')
mylist.delete_at_last()
mylist.print_all_elements()
print('\n')
mylist.delete_item(15)
mylist.print_all_elements()