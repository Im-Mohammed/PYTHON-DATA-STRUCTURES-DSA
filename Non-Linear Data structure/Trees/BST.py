class Node:
    def __init__(self,left,item,right):
        self.left=left
        self.item=item
        self.right=right

class BST:
    def __init__(self,root):
        self.root=root
    def insert_item(self,value):
        n=Node(None,value,None)
        if self.root is None:
            self.root=n
        else:
            temp=self.root
            while temp != None:
                if temp.item == value or temp.item < value:
                    if temp.right is None:
                        temp.right=n
                    temp=temp.right
                else:
                    if temp.left is None:
                        temp.left =n 
                    temp=temp.left
    def search(self,value):
        if self.root == None:
            raise IndexError("The Tree is empty")
        else:
            temp=self.root
            while temp!=None:
                if temp.item == value:
                    return temp
                elif temp.item < value:
                    temp=temp.left
                else:
                    temp=temp.right
            return None
    