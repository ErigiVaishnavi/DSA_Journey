n=2446
a=n
cnt=0
while(a>0):
    last=a%10
    if last==0:
        a//=10
        continue
    if n%last==0:
        cnt+=1
    a//=10      
print(cnt)
            