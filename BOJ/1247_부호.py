# 2023-11-28
import sys

for _ in range(3) :
    N = int(sys.stdin.readline())
    total = 0
    for n in range(N) : 
        num = int(sys.stdin.readline())
        total += num
    if total == 0 : sys.stdout.write("0\n")
    elif total > 0 : sys.stdout.write("+\n")
    else : sys.stdout.write("-\n")