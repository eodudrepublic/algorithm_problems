# 2023-04-08 (04-09)
import sys

def expand(n, s) :
    temp = [['*']*(4*n-3)]
    temp.append(['*']+[' ']*(4*n-5)+['*'])
    for l in s :
        temp.append(['*']+[' ']+l+[' ']+['*'])
    temp.append(['*']+[' ']*(4*n-5)+['*'])
    temp.append(['*']*(4*n-3))
    return temp
    
N = int(sys.stdin.readline())

star = [['*']]
for n in range(2, N+1) :
    star = expand(n, star)
for l in star :
    for s in l :
        print(s, end='')
    print()