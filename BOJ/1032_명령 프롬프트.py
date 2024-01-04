# 2024-01-04
import sys

N = int(sys.stdin.readline())
arr = []
for n in range(N) : arr.append(sys.stdin.readline())

L = len(arr[0])
arr[0] = list(arr[0])
for l in range(L) :
    tmp = arr[0][l]
    for n in range(N) : 
        if tmp != arr[n][l] :
            arr[0][l] = '?'
            break

for _ in arr[0] : sys.stdout.write(_)