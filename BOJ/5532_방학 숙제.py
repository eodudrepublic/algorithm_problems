# 2023-11-02 (11-03)
L = int(input())
A = int(input())
B = int(input())
a = int(input())
b = int(input())
math = A//a 
if A > a * math : math += 1
lang = B//b
if B > b * lang : lang += 1
if math > lang : print(L-math)
else : print(L-lang)