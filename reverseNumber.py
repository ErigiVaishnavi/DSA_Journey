N=987700
revN=0
while(N>0):
    last=N%10
    N=N//10
    revN=(revN*10)+last
print(revN) 