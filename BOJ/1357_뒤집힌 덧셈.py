# 2024-01-06
a, b = input().split()
a = a[::-1]
b = b[::-1]
sum = int(a) + int(b)
sum = int(str(sum)[::-1])
print(sum)