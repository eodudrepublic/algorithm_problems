# 2023-12-06 (12-07)
import sys

arr = list()
for _ in range(9) : arr.append(int(sys.stdin.readline()))

num = sum(arr) - 100
for _ in arr : 
    if (num - _) in arr and (num - _) != _ : 
        arr.remove(_)
        arr.remove(num - _)
        break

for _ in arr : 
    sys.stdout.write(''.join([str(_), '\n']))