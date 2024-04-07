# 2024-04-07
import sys

line = sys.stdin.readline().strip()
temp = 0
ans = 0
for _ in line :
    if _ == '(' :
        temp += 1
    else :
        if temp == 0 :
            ans += 1
        else :
            temp -= 1
ans += temp
sys.stdout.write(''.join([str(ans), '\n']))