# 2024-03-06 (03-07)
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n) :
    name, kor, eng, math = sys.stdin.readline().strip().split()
    arr.append([name, int(kor), int(eng), int(math)])
arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for _ in arr :
    sys.stdout.write(''.join([_[0], '\n']))