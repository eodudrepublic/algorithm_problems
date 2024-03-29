# 2024-03-29 (03-30)
import sys

ans = {0:'-'}
index = 0
lines = sys.stdin.readlines()
for line in lines :
    N = int(line)
    if N not in ans :
            for n in range(index, N) :
                blank = ' ' * (3**n)
                ans[n+1] = ''.join([ans[n], blank, ans[n]])
    index = N
    sys.stdout.write(''.join([ans[N], '\n']))