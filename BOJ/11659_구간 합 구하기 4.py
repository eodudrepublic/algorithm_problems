# 2024-04-03
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dic = {1:arr[0]}
for n in range(1, N) :
    dic[n+1] = arr[n] + dic[n]
for m in range(M) :
    i, j = map(int, sys.stdin.readline().split())
    if i == 1 : ans = dic[j]
    else : ans = dic[j] - dic[i-1]
    sys.stdout.write(''.join([str(ans), '\n']))