# 2023-08-20
import sys

N = int(sys.stdin.readline())
for n in range(N) :
    nums = list(map(int, sys.stdin.readline().split()))
    even = [_ for _ in nums if _ % 2 == 0]
    even.sort()
    sys.stdout.write(''.join([str(sum(even)), ' ', str(even[0]), '\n']))