# 2023-06-04
import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
for _ in combinations_with_replacement(arr, M) :
    print(*_)