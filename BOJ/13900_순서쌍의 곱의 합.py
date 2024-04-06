# 2024-04-06 (04-07)
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
temp = arr[0]
ans = 0
for n in range(1, N) :
    ans += temp * arr[n]
    temp += arr[n]
sys.stdout.write(''.join([str(ans), '\n']))