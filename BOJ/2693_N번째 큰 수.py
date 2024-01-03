# 2024-01-03
import sys

N = int(sys.stdin.readline())
for n in range(N) :
    arr = sorted(map(int, sys.stdin.readline().split()))
    print(arr[-3])