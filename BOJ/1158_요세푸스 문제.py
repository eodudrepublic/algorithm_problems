# 2023-06-19 (06-20)
import sys

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())
arr = list(range(1, N+1))
n = k = 0

ans = []
while arr :
    if k == K-1 :
        ans.append(str(arr[n]))
        del arr[n]
        k = 0
        N -= 1
        if n == N : n = 0
    else : 
        k += 1
        if n == N-1 : n = 0
        else : n += 1

print('<')
print(', '.join(ans))
print('>\n')