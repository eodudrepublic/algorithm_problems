# 2023-11-14 (11-15)
import sys

arr = []
temp = []
for _ in range(9) : 
    l = list(map(int, sys.stdin.readline().split()))
    arr.append(l)
    temp.append(max(l))

max = max(temp)
index = temp.index(max)
sys.stdout.write(''.join([str(max), '\n', str(index+1), ' ', str(arr[index].index(max)+1), '\n']))