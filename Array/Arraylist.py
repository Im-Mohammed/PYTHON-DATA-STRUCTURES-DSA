from array import *
a=array('i',[12,1,120,13])
print(sorted(a))
# 2 problem 
l=[1,'a',2,'c',3.2]
for i in l:
    if isinstance(i,int):
        continue
    else:
        l.remove(i)
print(l)
#3 calculate the average 
l=[1,2,3,4,5]
avg=sum(l)/len(l)
print(avg)
#4 create a list of N prime number 
n=int(input("ENter the number:  "))
count=0
for i in range(n+1):
    for j in range(2,n):
          if (i % j) ==0:
              count+=1
          if count==2:
              print(i)
  