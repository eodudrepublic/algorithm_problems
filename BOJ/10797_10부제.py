# 2023-06-26
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sys.stdout.write(''.join([str(arr.count(N)), '\n']))