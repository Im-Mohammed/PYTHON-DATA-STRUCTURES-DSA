"""  
Write a Recursive Function to calculate sum of First n Odd Number 
fun(n)
1. Task is to find sum of odd 
 if n %2 !=0:(refering to above )
2. Recurseive case i.e n+fun(n-1)
3. base case i.e if n > 0

"""
def Oddsum(n):
    if n >0 :
        if n % 2 != 0:
            s=n+Oddsum(n-1)
        else:
            Oddsum(n-1)
        return s

r=Oddsum(10)
print("The sum of first n odd numbers is",r)