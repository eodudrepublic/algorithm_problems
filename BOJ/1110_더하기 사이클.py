# 2023-05-19 (05-20)
import sys

N = int(sys.stdin.readline())

cycle = 0
n = N
while True :
    cycle += 1
    Nt = list(str(n))
    temp1 = Nt[-1]
    t = 0
    for i in Nt :
        t += int(i)
    T = list(str(t))
    temp2 = T[-1]
    temp = temp1 + temp2
    n = int(temp)
    if n == N :
        break

print(cycle)