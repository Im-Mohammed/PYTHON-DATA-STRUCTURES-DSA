'''
Recursive Function to print First N natural Numbers
'''
def Natural(n):
    if n==1:
        return 1
    return n+Natural(n-1)
'''
Every Recursive function has two cases:
1. Recursive Case:- It is a situation where the function is called again but with little easier task
2. Base Case :- It is a situation where the function is not called but instead it returns the value.
'''
#Driver Code
r=Natural(9)
print("The Sum Of Natural Numbers is :",r)
r=Natural(100)
print("The Sum Of Natural Numbers is :",r)
