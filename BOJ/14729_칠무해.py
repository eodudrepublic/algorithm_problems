# 2024-02-19
import sys

N = int(sys.stdin.readline())
ans = sorted(list(float(sys.stdin.readline()) for n in range(N)))
for _ in range(7) :
    print(f"{ans[_]:.3f}")