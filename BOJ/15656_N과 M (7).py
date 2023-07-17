# 2023-06-03
import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
for _ in product(arr, repeat=M) :
    print(*_)