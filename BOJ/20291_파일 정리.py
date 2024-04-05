# 2024-04-05 (04-06)
import sys

N = int(sys.stdin.readline())
ans = {}
for n in range(N) :
    name, ex = sys.stdin.readline().strip().split('.')
    if ex in ans :
        ans[ex] += 1
    else :
        ans[ex] = 1

keys = sorted(ans.keys())
for key in keys :
    sys.stdout.write(''.join([key, ' ', str(ans[key]), '\n']))