# 2023-07-29 (07-30)
import sys

N = int(sys.stdin.readline())
ans = 0
for n in range(1, N+1) :
    ans += n
sys.stdout.write(''.join([str(ans), '\n']))