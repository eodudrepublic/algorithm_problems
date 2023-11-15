# 2023-11-15 (11-16)
import sys

arr = []
for _ in range(5) :
    a, b, c, d = map(int, sys.stdin.readline().split())
    arr.append(a+b+c+d)
sys.stdout.write(''.join([str(arr.index(max(arr))+1), ' ', str(max(arr)), '\n']))