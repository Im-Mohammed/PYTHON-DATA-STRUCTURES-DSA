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
                    temp=temp.right
                elif temp.item > value:
                    temp=temp.left
                else:
                    temp=temp
            if temp.item > value:
                temp.left=n
            else:
                temp.right=n