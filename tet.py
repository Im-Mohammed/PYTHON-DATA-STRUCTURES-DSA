'''
arr=[0,1,2,3,4,5]
temp=[0]*(len(arr)-1)
print(temp[0])
print(temp[4])
c=[1,2,3]
d=[3,4]
print(c+d)
'''
def Rotate(arr):
    arr=arr[::-1]
    print(arr)
    arr=[arr[0]]+arr[:0:-1]
    print(arr)
arr1=[1,2,3,4,5]
Rotate(arr1)

a1=[1,2,3,4]
b=[3,2,5,6]
c=[3,4,8,9]
d=a1+b+c
print(d)
f=list(set(d))
print(f)

sentence=["alice and bob love leetcode","i think so too","this is great thanks very much"]
a=[]
for i in sentence:
    count=0
    for j in i:
        if j ==" ":
            count+=1
    a.append(count+1)
print(a)
print(max(a))
class Solution:
    def leaders(self, arr):
        # code here
        i=0
        j=len(arr)-1
        a=[]
        while i <= j:
            if arr[i] > arr[j]:
                j-=1
            elif arr[i] < arr[j]:
                i+=1
                j=len(arr)-1
            else:
                a.append(arr[i])
                i+=1
                j=len(arr)-1
        return a

obj=Solution()
res=obj.leaders([16 ,17, 4, 3, 5, 2])
print(res)
def StringCount(s):
    s=s.lower()
    count=0
    prev=s[0]
    for i in s:
        if prev!=i:
            count+=1
    return count 
StringCount()