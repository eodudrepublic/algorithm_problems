# 2023-06-02
import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
for _ in permutations(arr, M) :
    print(*_)