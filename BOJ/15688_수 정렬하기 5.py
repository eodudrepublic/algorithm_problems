# 2024-02-13
import sys

n = int(sys.stdin.readline())
arr = sorted(list(int(sys.stdin.readline()) for _ in range(n)))
for _ in arr : 
    sys.stdout.write(''.join([str(_), '\n']))