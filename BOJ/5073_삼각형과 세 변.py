# 2024-04-23 (04-24)
while True :
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 : break
    m = max(a, b, c)
    total = a + b + c
    if total - m <= m :
        print("Invalid")
    elif a == b and b == c and c == a :
        print("Equilateral")
    elif a != b and b != c and c != a :
        print("Scalene")
    else :
        print("Isosceles")