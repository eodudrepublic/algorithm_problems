# 2023-06-20
import sys

input = sys.stdin.readline
print = sys.stdout.write

S = input().strip()
arr = sorted([S[_:] for _ in range(len(S))])
for _ in arr :
    print(_)
    print('\n')