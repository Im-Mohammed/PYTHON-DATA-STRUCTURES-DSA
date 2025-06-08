class SumofSquare:
    def sumsquare(self,n):
        if n ==1 :
            return 1 
        return n*n + self.sumsquare(n-1)
    
st=SumofSquare()

print(st.sumsquare(3))