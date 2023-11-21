# 2023-11-21
import sys

N = int(sys.stdin.readline())
for n in range(N) :
    arr = list(sys.stdin.readline())
    arr[0] = arr[0].upper()
    for _ in arr : sys.stdout.write(_)