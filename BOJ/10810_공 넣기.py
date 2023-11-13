# 2023-11-13
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(N)]
for m in range(M) :
    i, j, k = map(int, sys.stdin.readline().split())
    for _ in range(i-1, j) : arr[_] = k
for _ in arr : sys.stdout.write(''.join([str(_), ' ']))
sys.stdout.write('\n')