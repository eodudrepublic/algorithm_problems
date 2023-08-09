# 2023-08-09 (08-10)
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ex = 0
p = 0
for _ in arr : 
    if _ == 0 : ex = 0
    else :
        ex += 1
        p += ex
print(p)