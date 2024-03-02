# 2024-03-02 (03-03)
import sys

arr = sorted(sys.stdin.readline().strip(), reverse=True)
total_sum = 0
for _ in arr :
    total_sum += int(_)
    total_sum = total_sum % 3
if '0' not in arr or total_sum != 0 :
    sys.stdout.write('-1\n')
else :
    index = arr.index('0')
    for _ in range(len(arr)) :
        if _ != index :
            sys.stdout.write(arr[_])
    sys.stdout.write('0\n')