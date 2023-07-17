# 2023-05-15 (05-16)
import sys

li = [0]
for i in range(8) :
    li.append(int(sys.stdin.readline()))

sorted_li = li.copy()
sorted_li.sort(reverse=True)
sorted_li = sorted_li[0:5]

sys.stdout.write(''.join([str(sum(sorted_li)), '\n']))
for i in range(1, 9) :
    if li[i] in sorted_li :
        sys.stdout.write(''.join([str(i), ' ']))
sys.stdout.write('\n')