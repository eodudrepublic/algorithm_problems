# 2023-08-18 (08-19)
import sys

N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())
sum = 0
for _ in arr : sum += int(_)
sys.stdout.write(''.join([str(sum), '\n']))