# 2023-10-19 (10-20)
while True :
    a, b, c = input().split()
    if a == '#' and b == '0' and c == '0' : break
    _b = int(b)
    _c = int(c)
    if _b <= 17 and _c < 80 : print(a, 'Junior')
    else : print(a, 'Senior')