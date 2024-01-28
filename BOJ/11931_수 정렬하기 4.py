# 2024-01-28
import sys

arr = []
N = int(sys.stdin.readline())
for n in range(N) : arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True)
for _ in arr : sys.stdout.write(''.join([str(_), '\n']))