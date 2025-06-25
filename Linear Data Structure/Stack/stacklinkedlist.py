class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.start==None
    def push(self,value):
        n=Node(value,self.start)
        self.start=n
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        return self.start.item
    def size(self):
        return self.item_count

st=Stack()
st.push(10)
st.push(20)
st.push(30)
print(st.peek())
print("The pop element is: ",st.pop())
print(st.peek())
print(st.size())