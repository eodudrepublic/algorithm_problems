# 2023-09-06 (09-07)
import sys

std = (1, 1, 2, 2, 2, 8)
arr = list(map(int, sys.stdin.readline().split()))
for _ in range(6) :
    sys.stdout.write(''.join([str(std[_] - arr[_]), ' ']))
sys.stdout.write('\n')