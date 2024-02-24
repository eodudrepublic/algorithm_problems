# 2024-02-24 (02-25)
import sys

N = int(sys.stdin.readline())
nSum = sum(range(1, N))

input_txt = sys.stdin.readline().rstrip()
totalSum = 0
temp = ''
for _ in input_txt :
    if _.isdigit() :
        temp += _
    else :
        totalSum += int(temp)
        temp = ''
totalSum += int(temp)
sys.stdout.write(''.join([str(totalSum - nSum), '\n']))