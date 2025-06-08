'''
Write a recursive function to print  odd natural Numbers upto given n value 
'''
def Oddnat(n):
    if n >0:
        Oddnat(n-1)
        if n % 2 !=0:
            print(n,end=" ")
#another way 
'''
Write a recursive function to print first n  odd natural Numbers 
'''
def Oddnat2(n):
    if n > 0:
        Oddnat2(n-1)
        print(2*n-1,end=" ")
  
print('\n')
Oddnat2(10)
#Driver Code 
'''
THe recursive case Oddnat(n-1) where as base case is n>0
THe condition for odd is n%2!=0 
'''
print('\n')
Oddnat(5)
'''
Write a recursive function to print  odd natural Numbers upto given n value in reverse Order
'''
print('\n')
def Oddnatrev(n):
    if n> 0:
        if n % 2 != 0:
            print(n,end=" ")
        Oddnatrev(n-1)
#Driver Code 
Oddnatrev(5)
'''
Write a recursive function to print first n odd natural Numbers in reverse Order
'''
#another way 
def Oddnat2rev(n):
    if n > 0:
        print(2*n-1,end=" ")
        Oddnat2rev(n-1)
  
print('\n')
Oddnat2rev(10)
#Driver Code 