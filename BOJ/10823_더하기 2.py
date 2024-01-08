# 2024-01-08
import sys

l = sys.stdin.readlines()
line = ''
for _ in l : line = ''.join([line, _.rstrip()]) 
arr = map(int, line.split(','))
print(sum(arr))