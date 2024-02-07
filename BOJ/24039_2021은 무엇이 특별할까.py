# 2024-02-07
def is_prime(n) :
    for _ in range(2, n) :
        if n % _ == 0 : return False
    return True

N = int(input())
a = 2
b = 3
while True :
    if a * b > N : break
    a = b
    while True :
        b += 2
        if is_prime(b) : break
print(a*b)