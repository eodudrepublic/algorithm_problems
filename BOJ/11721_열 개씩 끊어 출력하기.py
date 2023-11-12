# 2023-11-12
import sys

word = sys.stdin.readline().rstrip()
i = 0
for _ in word :
    sys.stdout.write(_)
    i += 1
    if i == 10 : 
        sys.stdout.write('\n')
        i = 0