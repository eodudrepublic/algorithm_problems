# 2023-05-05
import sys

N = int(sys.stdin.readline())

li = []
s = []
for n in range(N) :
    w, h = map(int, sys.stdin.readline().split())
    li.append([w, h])
    s.append([w, h])

s.sort(reverse=True)
for i in li :
    J = s.index(i)
    grade = 0
    for j in range(J+1) :
        if i[0] < s[j][0] and i[1] < s[j][1] :
            grade += 1
    sys.stdout.write(''.join([str(grade+1), ' ']))
sys.stdout.write('\n')
