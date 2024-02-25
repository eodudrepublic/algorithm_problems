# 2024-02-25
import sys

N, M = map(int, sys.stdin.readline().split())
s = set()
for n in range(N) :
    s.add(sys.stdin.readline())
ans = 0
for m in range(M) :
    temp = sys.stdin.readline()
    if temp in s :
        ans += 1
sys.stdout.write(''.join([str(ans), '\n']))