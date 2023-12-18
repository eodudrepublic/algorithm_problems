# 2023-12-18 (12-19)
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [_ for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    arr[a], arr[b] = arr[b], arr[a]
for _ in range(1, N+1) :
    sys.stdout.write(str(arr[_]))
    sys.stdout.write(' ')
sys.stdout.write('\n')