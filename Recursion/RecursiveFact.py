def Factorial(n):
    if n ==1 :
        return 1 
    return n * Factorial(n-1)

d=Factorial(3)
print("The factorial is : ",d)

print('\n')
def Fact(m):
    return 1 if m==1 else m * Fact(m-1)
t=Fact(3)
print(t)