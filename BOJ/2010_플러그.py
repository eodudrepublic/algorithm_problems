# 2023-08-11 (08-12)
import sys

N = int(sys.stdin.readline())

c = 0
for _ in range(N-1) :
    n = int(sys.stdin.readline())
    c += n - 1
c += int(sys.stdin.readline())
print(c)