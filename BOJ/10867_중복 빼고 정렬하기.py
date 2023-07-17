# 2023-06-10 (06-11)
import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
set = set(map(int, input().split()))
print(' '.join([str(_) for _ in sorted(set)]))
print('\n')