class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Deque:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.item_count=0
    def is_empty(self):
        return self.front is None
    def insert_front(self,value):
        n=Node(None,value,None)
        if not self.is_empty():
            self.front.prev=n
            n.next=self.front
        else:
            self.rear=n
        self.front=n
        self.item_count+=1   
    def insert_last(self,value):
        n=Node(None,value,None)
        if not self.is_empty():
            self.rear.next=n
            n.prev=self.rear
        else:
            self.front=n
        self.rear=n
        self.item_count+=1
        
    def delete_first(self):
        if not self.is_empty():
            self.front=self.front.next
            self.front.prev=None
            self.item_count-=1
        else:
            raise IndexError("Deque is empty")
    def delete_last(self):
        if not self.is_empty():
            self.rear=self.rear.prev
            self.rear.next=None
            self.item_count-=1
        else:
            raise IndexError("Deque Underflow")
    def get_front(self):
        return self.front.item
    def get_rear(self):
        return self.rear.item
    def size(self):
        return self.item_count
#Driver Code
st=Deque()
st.insert_front(20)
st.insert_last(30)
st.insert_front(40)
st.insert_last(50)
print("The front element before deletion: ",st.get_front())
print("The rear element before deletion: ",st.get_rear())
st.delete_first()
print("After deletion at front: ",st.get_front())
st.delete_last()
print("After deletion at last: ",st.get_rear())
print("The size of deque is : ",st.size())