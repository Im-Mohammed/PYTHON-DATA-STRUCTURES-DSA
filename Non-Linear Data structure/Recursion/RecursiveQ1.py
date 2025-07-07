##Recursive Function to print First N natural Numbers
def Natural(n):
    if n > 0:
        Natural(n-1)
        print(n,end=" ")

# Driver Code 
Natural(10)
print('\n')
##Recursive Function to print First N natural Numbers in Reverse Order
def revNatural(n):
    if n >0:
        print(n,end=" ")
        revNatural(n-1)
#Driver Code 
revNatural(10)
