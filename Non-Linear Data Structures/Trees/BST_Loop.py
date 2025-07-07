class Node:
    def __init__(self,left,item,right):
        self.left=left
        self.item=item
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root
    def insert_item(self,value):
        n=Node(None,value,None)
        if self.root is None:
            self.root=n
        else:
            temp=self.root
            while temp is not None:
                if temp.item == value or temp.item < value:
                    if temp.right is None:
                        temp.right=n
                        break
                    temp=temp.right
                else:
                    if temp.left is None:
                        temp.left =n 
                        break
                    temp=temp.left
    def search(self,value):
        if self.root == None:
            raise IndexError("The Tree is empty")
        else:
            temp=self.root
            while temp!=None:
                if temp.item == value:
                    return temp
                elif value < temp.item  :
                    temp=temp.left
                else:
                    temp=temp.right
        return False
    def inorder(self):
        temp=self.root
        stack=[]
        while True:
            if temp is not None:
                stack.append(temp)
                temp=temp.left
            elif stack:
                temp=stack.pop()
                print(temp.item,end=" ")
                temp=temp.right
            else:
                break
    def preorder(self):
        temp = self.root
        stack=[]
        while True:
            if temp is not None:
                if temp.left is not None or temp.right is not None:
                    stack.append(temp)
                print(temp.item,end=" ")
                temp=temp.left
            elif stack:
                temp=stack.pop()
                if temp.right is not None:
                    temp=temp.right
            else:
                break
    def postorder(self):
        temp=self.root
        stack=[]
        while True:
            if temp is not None:
                stack.append(temp)
                temp=temp.left
            elif stack:
                peek=stack[-1]
                if peek.right is not None and last_visited != peek.right:
                    temp=peek.right
                else:
                    print(peek.item,end=" ")
                    last_visited=stack.pop()
            else:
                break

ob=BST()
ob.insert_item(50)
ob.insert_item(60)
ob.insert_item(30)
ob.insert_item(40)
ob.insert_item(20)
ob.insert_item(70)
ob.insert_item(55)
t=ob.search(40)
print(t.item)
ob.inorder()
print('\n')
ob.preorder()
print('\n')
ob.postorder()