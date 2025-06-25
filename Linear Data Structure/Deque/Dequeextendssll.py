from LinkedList.dll import *
class Deque(dll):
    def __init__(self,front=None,rear=None):
        super().__init__(front)
        self.item_count=0
        self.rear=rear
    def is_empty():
        return super().is_empty()
    def insert_front(self,value):
        self.insert_at_start(value)
        self.item_count+=1
    def insert_last(self,value):
        self.rear=self.insert_at_last(value)
        self.item_count+=1
    def delete_front(self):
        self.delete_at_first()
        self.item_count-=1
    def delete_last(self):
        self.rear=self.delete_at_last()
        self.item_count-=1
    def get_front(self):
        return self.start.item
    def get_rear(self):
        return self.rear.item
    def size(self):
        return self.item_count
#driver code
st=Deque()
st.insert_front(20)
st.insert_last(30)
st.insert_front(40)
st.insert_last(50)
print(st.get_front())
print(st.get_rear())
st.delete_front()
print("After deletion at front: ")
print(st.get_front())
print("After deletion at last: ")
st.delete_last()
print(st.get_rear())
