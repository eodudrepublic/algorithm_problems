# 2023-09-25 (09-26)
import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
if a + b + c != 180 : sys.stdout.write('Error\n')
else : 
    if a == 60 and b == 60 : sys.stdout.write('Equilateral\n')
    elif a == b or b == c or c == a : sys.stdout.write('Isosceles\n')
    else : sys.stdout.write('Scalene\n')