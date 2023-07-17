# 2023-06-17 (06-18)
import sys

input = sys.stdin.readline

ESM = [1, 1, 1]
target = list(map(int, input().split()))

year = 1
while ESM != target :
    ESM[0] += 1
    if ESM[0] == 16 : ESM[0] = 1
    ESM[1] += 1
    if ESM[1] == 29 : ESM[1] = 1
    ESM[2] += 1
    if ESM[2] == 20 : ESM[2] = 1
    year += 1

print(year)