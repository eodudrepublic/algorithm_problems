# 2023-08-17 (08-18)
import sys

while True :
    code = sys.stdin.readline().rstrip()
    if code == 'END' : break
    reverse = list(code)
    reverse.reverse()
    sys.stdout.write(''.join(reverse))
    sys.stdout.write('\n')