# 2023-04-16 (04-17)
import sys

N = int(sys.stdin.readline())

pLi = []
for n in range(N) :
    pLi.append(int(sys.stdin.readline()))

pLi.sort()
for n in pLi :
    sys.stdout.write(str(n))
    sys.stdout.write('\n')
    # 이게 가장 빠르더라