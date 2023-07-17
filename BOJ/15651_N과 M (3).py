# 2023-05-31 (06-01)
import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(1, N+1))
for _ in product(arr, repeat=M) :
    print(*_)