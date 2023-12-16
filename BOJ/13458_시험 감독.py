# 2023-12-16 (12-17)
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())
total = 0
for _ in arr :
    if _ > a : _ -= a
    else : _ = 0
    total += 1 + _ // b
    if _ % b != 0: total += 1
print(total)

