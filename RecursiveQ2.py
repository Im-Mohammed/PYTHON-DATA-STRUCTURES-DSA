'''
Write a recursive function to print first n odd natural Numbers
'''
def Oddnat(n):
    if n >0:
        Oddnat(n-1)
        if n % 2 !=0:
            print(n,end=" ")
#Driver Code 
'''
THe recursive case Oddnat(n-1) where as base case is n>0
THe condition for odd is n%2!=0 
'''
Oddnat(5)
'''
Write a recursive function to print first n odd natural Numbers in reverse Order
'''
print('\n')
def Oddnatrev(n):
    if n> 0:
        if n % 2 != 0:
            print(n,end=" ")
        Oddnatrev(n-1)
#Driver Code 
Oddnatrev(5)