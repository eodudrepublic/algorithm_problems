# 2023-05-12 (05-13)
import sys

line = list(sys.stdin.readline().strip())
l = len(line)

cac = 0
for i in range(l-1, -1, -1) :
    if line[i] == -1 : continue
    cac += 1
    if line[i] == '-' :
        line[i-1] = -1
        continue
    if line[i] == '=' :
        if line[i-1] == 'c' or line[i-1] == 's' :
            line[i-1] = -1
        elif line[i-1] == 'z' :
            if i >= 2 and line[i-2] == 'd' :
                line[i-1] = -1
                line[i-2] = -1
            else :
                line[i-1] = -1
        continue
    if line[i] == 'j' and i >= 1 :
        if line[i-1] == 'n' or line[i-1] == 'l' :
            line[i-1] = -1

print(cac)