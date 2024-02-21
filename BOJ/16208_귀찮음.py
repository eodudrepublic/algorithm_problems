# 2024-02-21
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

total = 0
for _ in arr : total += _

ans = 0
for _ in arr :
    total -= _
    ans += _ * total

sys.stdout.write(''.join([str(ans), '\n']))