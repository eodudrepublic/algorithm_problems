# 2023-05-30 (05-31)
import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(1, N+1))
for _ in permutations(arr, M) :
    print(*_)