class SumofSquare:
    def sumsquare(self,n):
        if n ==1 :
            return 1 
        return n*n + self.sumsquare(n-1)
    
st=SumofSquare()

print(st.sumsquare(3))

# Using just function 
def Sumsquare(n):
    if n == 1 :
         return 1 
    return n*n + Sumsquare(n-1)

R=Sumsquare(4) 
print('The sum of squares is : ',R)
#1^2+2^2+3^2+4^2=1+4+9+16=30