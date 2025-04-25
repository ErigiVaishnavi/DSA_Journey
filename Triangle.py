a=5
for i in range(a):
    if i==0:
        print('* '+'  '*(a-1))
    elif i==a-1:
        print('*'*a)
    else:
        print('*'*(i+1)+'  '*(a-(i+1)))