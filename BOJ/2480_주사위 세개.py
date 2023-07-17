# 2023-05-03 (05-04)
import sys

dice = list(map(int, sys.stdin.readline().split()))

for i in dice :
    if dice.count(i) == 3 :
        print(10000+i*1000)
        sys.exit()
    elif dice.count(i) == 2 :
        print(1000+i*100)
        sys.exit()

print(max(dice)*100)