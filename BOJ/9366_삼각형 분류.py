# 2024-04-27 (04-28)
N = int(input())
for n in range(N) :
    a, b, c = map(int, input().split())
    temp = max(a, b, c)
    if a == b and b == c :
        print(f"Case #{n+1}: equilateral")
    elif a + b + c - temp <= temp :
        print(f"Case #{n+1}: invalid!")
    elif a == b or b == c or c == a :
        print(f"Case #{n+1}: isosceles")
    else :
        print(f"Case #{n+1}: scalene")