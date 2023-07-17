# 2023-04-10
import sys

N = int(sys.stdin.readline())

for n in range(N) :
    if n%2 == 0 :
        print('* '*N)
    else :
        print(' *'*N)