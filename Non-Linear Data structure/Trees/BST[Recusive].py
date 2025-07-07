class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root
    def insert(self,value):
        self.rinsert(self.root,value)
    def rinsert(self,root,value):
        if root is None:
            return Node(value)
        if value < root.item:
            root.left=self.rinsert(root.left,value)
        elif value > root.item:
            root.right = self.rinsert(root.right,value)
        return root
    def search(self,value):
        return self.rsearch(self.root,value)
    def rsearch(self,root,value):
        if root.item == value or root is None:
            return root
        if value < root.item :
            self.rsearch(root.left,value)
        elif value > root.item:
            self.rsearch(root.right,value)
    