class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root
    def insert(self,value):
        self.root=self.rinsert(self.root,value)
        print(self.root.item)
    def rinsert(self,root,value):
        if root is None:
            return Node(None,value)
        if value < root.item:
            root.left=self.rinsert(root.left,value)
        elif value > root.item:
            root.right = self.rinsert(root.right,value)
        return root
    def search(self,value):
        res=self.rsearch(self.root,value)
        if res is not None:
            return True
        return res
    def rsearch(self,root,value):
        if root is None or root.item == value:
            return root
        if value < root.item :
            return self.rsearch(root.left,value)
        elif value > root.item:
            return self.rsearch(root.right,value)
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root is not None:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root :
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
    def minimum(self):
        return self.rminimum(self.root)
    def rminimum(self,root):
        if root.left is None:
            return root.item
        return self.rminimum(root.left)
    def maximum(self):
        return self.rmaxi(self.root)
    def rmaxi(self,root):
        if root.right is None:
            return root.item
        return self.rmaxi(root.right)
    def delete(self,data):
        return self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.item :
            root.left=self.rdelete(root.left,data)
        elif data > root.item:
            root.right = self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.minimum(root.right)
            self.rdelete(root.right,root.item)
        return root
    
    
    
bst=BST()
bst.insert(50)
bst.insert(40)
bst.insert(30)
bst.insert(60)
bst.insert(70)
bst.insert(20)
bst.insert(80)
inorde1=bst.inorder()
print(inorde1)
print('\n')
se=bst.search(100)
print(se)
print('\n')
pre=bst.preorder()
print(pre)
print('\n')
post=bst.postorder()
print(post)
print('\n')
a=bst.minimum()
print("The minimum Element is : ",a)
b=bst.maximum()
print("The maximum element is : ",b)