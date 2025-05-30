from sll import *
class Stack(sll):
    item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,value):
        self.insertion_at_top(value)
        Stack.item_count+=1
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.delete_first()
            Stack.item_count-=1
        return data
    def peek(self):
        if not self.is_empty():
            data = self.start.item
        return data
    def size(self):
        return Stack.item_count
    def insert_at_last(self, value):
        raise AttributeError("Stack has no attribute insert at last")
    def insert_at_middle(self, temp, value):
        raise AttributeError("Stack has no attribute insert at middle")
    def delete_at_middle(self, temp):
        raise AttributeError("Stack has no attribute delete at middle")
    def delete_at_last(self):
        raise AttributeError("Stack has no attribute delete at middle")

st=Stack()
st.push(20)
st.push(30)
st.push(40)
st.pop()
print(st.peek())
print(st.size())
