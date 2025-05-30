class Queue:
    def __init__(self):
        self.mylist=[]
    def is_empty(self):
        return len(self.mylist)==0
    def push(self,value):
        self.mylist.insert(0,value)
    def pop(self):
        if not self.is_empty():
            return self.mylist.pop()
        else:
            raise IndexError("Index out of range")
    def rear(self):
        return self.mylist[len(self.mylist)-1]
    def front(self):
        return self.mylist[0] 
    def size(self):
        return len(self.mylist)

st=Queue()
st.push(10)
st.push(20)
st.push(30)
print("The element which is removed is : ",st.pop())
print("Rear value: ",st.rear())
print("Front Value:",st.front())
print(st.size())