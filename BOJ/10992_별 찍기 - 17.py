# 2023-04-10
import sys

N = int(sys.stdin.readline())

print(''.join([' '*(N-1), '*']))
for n in range(2, N) :
    print(''.join([' '*(N-n), '*', ' '*(2*n-3), '*']))
if N > 1 :
    print('*'*(2*N-1))  