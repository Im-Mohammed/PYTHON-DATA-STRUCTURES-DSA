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