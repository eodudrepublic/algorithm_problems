# 2023-11-20 (11-21)
import sys

while True :
    n = sys.stdin.readline().rstrip()
    if n == '0' : break
    size = 1
    for _ in n :
        if _ == '1' : size += 3
        elif _ == '0' : size += 5
        else : size += 4
    sys.stdout.write(''.join([str(size), '\n']))