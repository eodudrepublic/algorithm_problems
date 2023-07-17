# 2023-06-12 (06-13)
import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())

arr = deque(range(1, N+1))

i = 1
ans = []
while arr :
    a = arr.popleft()
    if i == K :
        ans.append(a)
        i = 1
        continue
    arr.append(a)
    i += 1

print('<')
print(', '.join([str(_) for _ in ans]))
print('>\n')