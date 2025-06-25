class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,value):
        self.append(value)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise Exception("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,value):
        raise AttributeError("Stack has no attribute 'insert' ")
    
st=Stack()
st.push(10)
st.push(20)
st.push(30)
st.pop()
print(st.peek())
print(st.size())
