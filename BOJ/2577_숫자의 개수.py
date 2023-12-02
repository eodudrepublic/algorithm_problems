# 2023-12-02
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

num = a * b * c
str_num = str(num)
arr = [0 for _ in range(10)]
for _ in str_num : arr[int(_)] += 1
for _ in arr : sys.stdout.write(''.join([str(_), '\n']))