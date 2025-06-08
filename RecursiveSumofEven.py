'''
Write a recursive function to calculate sum of first n even numbers 
'''
def Evensum(n):
    if n == 0:
        return 0
    return 2*n + Evensum(n-1)
#driver code 
r=Evensum(3)
print("The even sum is : ",r)
#2+4+6=12