# 2023-07-07 (07-08)
import sys

h, m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

tmp = m + t
m = tmp % 60
h = h + (tmp // 60)
if h >= 24 : h = h % 24

sys.stdout.write(''.join([str(h), ' ', str(m), '\n']))