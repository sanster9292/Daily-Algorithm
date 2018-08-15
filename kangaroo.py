vals = input().strip().split(' ')
x1, v1, x2,v2  = [int(i) for i in vals]

first = x1-x2
second = v2-v1

if (x1<x2) and (v1<v2):
    print('NO')
elif first%second ==0:
    print('YES')
elif (x1<x2) and v1<v2:
    print('NO')
elif v1==v2:
    print('NO')
