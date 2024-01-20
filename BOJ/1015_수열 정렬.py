# 2024-01-20
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = sorted(arr[:])
for _ in arr :
    index = ans.index(_)
    sys.stdout.write(''.join([str(index), ' ']))
    ans[index] = -1
sys.stdout.write('\n')