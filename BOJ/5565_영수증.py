# 2023-08-05
import sys

total = int(sys.stdin.readline())
price = 0
for _ in range(9) :
    price += int(sys.stdin.readline())
print(total-price)