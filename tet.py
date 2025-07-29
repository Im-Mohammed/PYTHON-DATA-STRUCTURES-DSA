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
    c=s.lower()
    print(c)
    count=0
    prev=s[0]
    print(prev)
    for i in c:
        if prev!=i:
            count+=1
            prev=i
    return count 
s="aAbBcC"
a=StringCount(s)
print(a)
def searchInSorted(arr, k):
    i=0
    j=len(arr)-1
    while i<= j:
        mid=(i+j)//2
        if arr[mid]==k:
           return True
        elif arr[mid] < k:
            i=mid+1
        else:
            j=mid
    return False
arr=[1,2,3,4,5,6]
k=6
b=searchInSorted(arr,k)
print(b)
#Maximum water container
def MaxWaterContainer(height):
    left=0
    right=len(height)-1
    max_area=0
    while left <= right:
        curarea=min(height[left],height[right])*(right-left)
        max_area=max(max_area,curarea)
        if height[left] < height[right]:
            left+=1
        else:
            right-=1
    return max_area
height=[1,8,6,2,5,4,8,3,7]
a=MaxWaterContainer(height)
print("The container with most water is : ",a)