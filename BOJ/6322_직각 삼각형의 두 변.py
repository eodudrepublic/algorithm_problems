# 2024-04-21 
i = 1
while True :
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 : break
    print(f"Triangle #{i}")
    if a == -1 :
        temp = c**2 - b**2
        if temp <= 0 :
            print("Impossible.\n")
        else :
            a = temp ** (1/2)
            print(f"a = {a:.3f}\n")
    elif b == -1 :
        temp = c**2 - a**2
        if temp <= 0 :
            print("Impossible.\n")
        else :
            b = temp ** (1/2)
            print(f"b = {b:.3f}\n")
    else :
        c = (a**2 + b**2)**(1/2)
        print(f"c = {c:.3f}\n")
    i += 1