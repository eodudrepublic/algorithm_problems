# 2024-01-22
import sys
import math

a, b = map(int, sys.stdin.readline().split())
sys.stdout.write(''.join([str(math.lcm(a, b)), '\n']))