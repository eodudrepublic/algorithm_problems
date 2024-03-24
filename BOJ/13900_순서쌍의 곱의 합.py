import sys
from itertools import combinations

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
for _ in combinations(arr, 2) :
    ans += _[0] * _[1]
sys.stdout.write(''.join([str(ans), '\n']))