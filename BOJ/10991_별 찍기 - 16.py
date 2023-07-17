# 2023-04-10
import sys

N = int(sys.stdin.readline())

print(''.join([' '*(N-1), '*']))
for n in range(2, N+1) :
    print(''.join([' '*(N-n), '* '*n]))