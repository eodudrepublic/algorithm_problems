# 2024-02-15
import sys

a, b = map(int, sys.stdin.readline().split())
ans = abs(a - b)
N = int(sys.stdin.readline())
for n in range(N) :
    c = int(sys.stdin.readline())
    temp = abs(b - c) + 1
    if ans > temp : ans = temp
sys.stdout.write(''.join([str(ans), '\n']))