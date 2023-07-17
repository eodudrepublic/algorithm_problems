# 2023-05-31 (06-01)
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(1, N+1))
for _ in combinations(arr, M) :
    print(*_)