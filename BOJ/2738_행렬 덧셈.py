# 2023-10-31
import sys

N, M = map(int, sys.stdin.readline().split())
arr1 = []
for n in range(N) : arr1.append(list(map(int, sys.stdin.readline().split())))

arr2 = []
for n in range(N) : arr2.append(list(map(int, sys.stdin.readline().split())))

for n in range(N) : 
    for m in range(M) : arr1[n][m] += arr2[n][m]

for line in arr1 : print(*line)