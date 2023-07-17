# 2023-06-01 (06-02)
import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(1, N+1))
for _ in combinations_with_replacement(arr, M) :
    print(*_)