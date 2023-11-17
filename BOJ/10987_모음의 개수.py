# 2023-11-17
import sys

arr = ('a', 'e', 'i', 'o', 'u')
ans = 0
line = sys.stdin.readline().rstrip()
for _ in line :
    if _ in arr : ans += 1
sys.stdout.write(''.join([str(ans), '\n']))