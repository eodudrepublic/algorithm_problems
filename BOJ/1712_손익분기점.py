# 2023-12-08
import sys

a, b, c = map(int, sys.stdin.readline().split())
if b >= c : sys.stdout.write('-1\n')
else : sys.stdout.write(''.join([str(a//(c-b)+1), '\n']))