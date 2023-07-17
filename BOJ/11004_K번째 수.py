# 2023-06-09 (06-10)
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = sorted(map(int, input().split()))
print(arr[K-1])