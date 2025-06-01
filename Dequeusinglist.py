class deque:
    def __init__(self):
        self.mylist=[]
    def insert_front(self,value):
        self.mylist.insert(0,value)
    def insert_last(self,value):
        self.mylist.append(value)
    def delete_front(self):
        self.mylist.pop(0)
    def delete_last(self):
        self.mylist.pop()
    def get_front(self):
        return self.mylist[0]
    def get_rear(self):
        return self.mylist[-1]
    def size(self):
        return len(self.mylist)
    
#driver code
st=deque()
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
