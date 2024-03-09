# 2024-03-09
import sys

def func() :
    line = sys.stdin.readline().strip()
    ans = 0
    for _ in line :
        if _ == '(' :
            ans += 1
        elif _ == ')' :
            ans -= 1
        else : pass
        if ans < 0 : break
    if ans != 0 : sys.stdout.write('NO\n')
    else : sys.stdout.write('YES\n')

N = int(sys.stdin.readline())
for n in range(N) :
    func()