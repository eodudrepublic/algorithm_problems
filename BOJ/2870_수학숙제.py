# 2024-03-22 (03-23)
import sys

ans = []
N = int(sys.stdin.readline())
for n in range(N) :
    temp = []
    line = sys.stdin.readline().strip()
    for _ in line :
        if _.isdigit() :
            temp.append(_)
        else :
            if temp :
                num = int(''.join(temp))
                ans.append(num)
                temp.clear()
    if temp :
        num = int(''.join(temp))
        ans.append(num)
ans.sort()
for _ in ans :
    sys.stdout.write(''.join([str(_), '\n']))