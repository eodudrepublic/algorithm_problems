# 2023-07-10 (07-11)
import sys

N = int(sys.stdin.readline())
cute = 0
for n in range(N) :
    a = int(sys.stdin.readline())
    if a == 0 : cute -= 1
    else : cute += 1
if cute < 0 : sys.stdout.write('Junhee is not cute!\n')
else : sys.stdout.write('Junhee is cute!\n')