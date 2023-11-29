# 2023-11-29
import sys

arr = set()
for _ in range(10) :
    n = int(sys.stdin.readline())
    arr.add(n%42)
print(len(arr))