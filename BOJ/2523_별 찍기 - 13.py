# 2023-04-10
import sys

N = int(sys.stdin.readline())

for n in range(1, N+1):
    print('*'*n)
for n in range(N-1, 0, -1) :
    print('*'*n)