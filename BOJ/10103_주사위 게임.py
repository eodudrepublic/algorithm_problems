# 2023-07-19
import sys

N = int(sys.stdin.readline())
A = B = 100
for n in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    if a > b : B -= a
    elif a < b : A -= b
    else : pass

print(A)
print(B)