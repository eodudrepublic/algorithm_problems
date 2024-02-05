# 2024-02-05
def gcd(a, b) : 
    while b > 0 :
        a, b = b, a % b
    return a

m, n = map(int, input().split(':'))
g = gcd(m, n)
print(f'{m//g}:{n//g}')