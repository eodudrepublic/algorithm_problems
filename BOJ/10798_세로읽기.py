# 2024-01-02
import sys

a = sys.stdin.readline().rstrip()
la = len(a)
b = sys.stdin.readline().rstrip()
lb = len(b)
c = sys.stdin.readline().rstrip()
lc = len(c)
d = sys.stdin.readline().rstrip()
ld = len(d)
e = sys.stdin.readline().rstrip()
le = len(e)
for i in range(15) :
    if i < la : sys.stdout.write(a[i])
    if i < lb : sys.stdout.write(b[i])
    if i < lc : sys.stdout.write(c[i])
    if i < ld : sys.stdout.write(d[i])
    if i < le : sys.stdout.write(e[i])
sys.stdout.write('\n')