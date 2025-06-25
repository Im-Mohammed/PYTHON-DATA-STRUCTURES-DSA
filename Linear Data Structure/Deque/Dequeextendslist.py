class Deque(list):
    def is_empty(self):
        return len(self)==0
    def insert_front(self,value):
        self.insert(0,value)
    def insert_last(self,value):
        self.append(value)
    def delete_first(self):
        if not self.is_empty():
            self.pop(0)
        else:
            raise IndexError("Deque is empty")
    def delete_last(self):
        if not self.is_empty():
            self.pop()
        else:
            raise IndexError("Deque is empty")
    def get_front(self):
        return self[0]
    def get_rear(self):
        return self[-1]
    def size(self):
        return len(self)

#driver code
st=Deque()
st.insert_front(20)
st.insert_last(30)
st.insert_front(10)
st.insert_last(50)
print(st.get_front())
print(st.get_rear())
st.delete_first()
print("After deletion at front: ")
print(st.get_front())
print("After deletion at last: ")
st.delete_last()
print(st.get_rear())