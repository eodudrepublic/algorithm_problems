# 2023-04-25 (04-26)
import sys

N = int(sys.stdin.readline())

mem_list = []
for n in range(N) :
    age, name = sys.stdin.readline().split()
    mem_list.append([int(age), n, name])

mem_list.sort()
for m in mem_list :
    sys.stdout.write(''.join([str(m[0]), ' ', m[-1], '\n']))