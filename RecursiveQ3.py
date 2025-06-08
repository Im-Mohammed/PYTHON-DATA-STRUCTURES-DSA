'''
Write a recursive function to print first n Even natural Numbers
'''
def EvenNat(n):
    if n > 0:
        EvenNat(n-1)
        if n % 2 ==0:
            print(n,end=" ")
#Drive Code
EvenNat(10)
print('\n')
'''
Write a recursive function to print first n Even natural Numbers in reverse order 
'''
def Evenatrev(n):
    if n > 0:
        if n % 2 ==0:
            print(n,end=" ")
        Evenatrev(n-1)
#Driver Code
Evenatrev(10)
