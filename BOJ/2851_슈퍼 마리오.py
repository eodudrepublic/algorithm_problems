# 2024-01-11
import sys

arr = []
for _ in range(10) : arr.append(int(sys.stdin.readline()))

ans = 0
for _ in arr :
    temp = ans + _
    if abs(100 - temp) > abs(100 - ans) : break
    else : ans = temp
sys.stdout.write(''.join([str(ans), '\n']))