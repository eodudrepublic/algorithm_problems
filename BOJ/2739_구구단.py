# 2023-08-04 (08-05)
import sys

N = int(sys.stdin.readline())
for n in range(1, 10) :
    sys.stdout.write(''.join([str(N), ' * ', str(n), ' = ', str(N*n), '\n']))