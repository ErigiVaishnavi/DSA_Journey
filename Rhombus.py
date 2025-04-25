a=4
for i in range(a):
    spaces=' '*i
    print(spaces+'*'*a)

a=4
for i in range(a):
    spaces=' '*(a-i)
    print(spaces+'*'*a)