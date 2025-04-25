N=121
revN=0
dup=N
while(N>0):
    last=N%10
    N=N//10
    revN=(revN*10+last)
if dup==revN:
    print(True)
else:
    print(False)