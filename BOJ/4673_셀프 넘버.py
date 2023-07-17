# 2023-05-17
import sys

def d(n) :
    dn = n
    num = list(str(n))
    for i in num :
        dn += int(i)
    return dn

li = list(range(1, 10001))
for n in range(1, 10001) :
    if d(n) in li :
        li.remove(d(n))

for i in li :
    sys.stdout.write(str(i))
    sys.stdout.write('\n')