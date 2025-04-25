a=int(input())

for i in range(a):
    if i==0:
        print('* '*a)
    elif i==(a-1):
        print('* '*a)
    else:
        print('* '+'* '*(a-2)+'*')
