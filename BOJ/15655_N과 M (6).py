# 2023-06-03
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
for _ in combinations(arr, M) :
    print(*_)