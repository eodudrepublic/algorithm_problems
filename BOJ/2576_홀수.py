# 2023-08-02 (08-03)
import sys

arr = []
for _ in range(7) : arr.append(int(sys.stdin.readline()))
odds = [_ for _ in arr if _ % 2 == 1]
if not odds : sys.stdout.write('-1\n')
else :
    odds.sort()
    sys.stdout.write(''.join([str(sum(odds)), '\n', str(odds[0]), '\n']))