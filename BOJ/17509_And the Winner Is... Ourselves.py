# 2024-02-20 (02-21)
import sys

time = []
error = []
for _ in range(11) :
    d, v = map(int, sys.stdin.readline().split())
    time.append(d)
    error.append(v)
time.sort()

ans = 0
for _ in error :
    ans += 20 * _
t = 0
for _ in time :
    t += _
    ans += t
sys.stdout.write(''.join([str(ans), '\n']))