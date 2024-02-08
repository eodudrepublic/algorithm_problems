# 2024-02-08
import sys

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
sorted_arr = sorted(arr)
reversed_arr = sorted(arr, reverse=True)
if arr == sorted_arr : sys.stdout.write('INCREASING\n')
elif arr == reversed_arr : sys.stdout.write('DECREASING\n')
else : sys.stdout.write('NEITHER\n')