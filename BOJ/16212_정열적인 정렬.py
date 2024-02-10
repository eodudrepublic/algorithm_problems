# 2024-02-10
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for _ in sorted(arr) : sys.stdout.write(''.join([str(_), ' ']))
sys.stdout.write('\n')