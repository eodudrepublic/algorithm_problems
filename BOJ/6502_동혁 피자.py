# 2024-04-17 (04-18)
import sys

index = 1
r2 = 2 ** (1/2)
while True : 
    line = sys.stdin.readline()
    if line[0] == '0' :
        break
    r, w, l = map(int, line.split())
    if 4 * (r**2) >= (w**2) + (l**2) :
        sys.stdout.write(''.join(['Pizza ', str(index), ' fits on the table.\n']))
    else :
        sys.stdout.write(''.join(['Pizza ', str(index), ' does not fit on the table.\n']))
    index += 1