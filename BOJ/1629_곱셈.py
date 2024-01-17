# 2024-01-17
a, b, c = map(int, input().split())

dict = {0 : 1, 1 : a%c}

def mul(x) :
    if x % 2 != 0 : return ((mul(x - 1) % c) * dict[1]) % c
    
    try :
        return dict[x]
    except :
        dict[x] = ((mul(x//2) % c) * (mul(x//2) % c)) % c
        return dict[x]

ans = mul(b)
print(ans)