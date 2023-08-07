# 2023-08-07 (08-08)
import sys

arr = [1, 1]
f = 1
N = int(sys.stdin.readline())
for _ in range(2, N+1) :
    f *= _
    arr.append(f)
sys.stdout.write(''.join([str(arr[N]), '\n']))