"""  
Write a Recursive Function to calculate sum of First n Odd Number 
fun(n)
1. Task is to find sum of odd 
2. Recurseive case i.e n+fun(n-1)
3. base case i.e if n > 0

"""
def Oddsum(n):
    if n ==1 :
        return 1
    s=2*n-1
    return s + Oddsum(n-1)

r=Oddsum(3)
print("The sum of first n odd numbers is",r)