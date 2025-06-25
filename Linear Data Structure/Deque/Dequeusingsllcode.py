from LinkedList.dll import *
class deque:
    def __init__(self,rear=None):
        self.obj=dll()
        self.rear=rear
        self.item_count=0
    def is_empty(self):
        return self.obj.is_empty()
    def insert_front(self,value):
        self.obj.insert_at_start(value)
        self.item_count+=1
    def insert_last(self,value):
        self.rear=self.obj.insert_at_last(value)
        self.item_count+=1
    def delete_first(self):
        self.obj.delete_at_first()
        self.item_count-=1
    def delete_last(self):
        self.rear=self.obj.delete_at_last()
        self.item_count-=1
    def get_front(self):
        return self.obj.start.item
    def get_rear(self):
        return self.rear.item
    def size(self):
        return self.item_count
    
#driver code
st=deque()
st.insert_front(20)
st.insert_last(30)
st.insert_front(40)
st.insert_last(50)
print(st.get_front())
print(st.get_rear())
st.delete_first()
print("After deletion at front: ")
print(st.get_front())
print("After deletion at last: ")
st.delete_last()
print(st.get_rear())
    