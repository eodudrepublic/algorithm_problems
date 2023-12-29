# 2023-12-29 (12-30)
import sys

N = int(sys.stdin.readline())
for n in range(N) :
    pw = sys.stdin.readline().rstrip()
    if len(pw) >= 6 and len(pw) <= 9 : sys.stdout.write('yes\n')
    else : sys.stdout.write('no\n')