# 2023-06-24 (06-25)
import sys

total = 0
for _ in range(5) :
    s = int(sys.stdin.readline())
    if s >= 40 :
        total += s
    else :
        total += 40

sys.stdout.write(''.join([str(total//5), '\n']))