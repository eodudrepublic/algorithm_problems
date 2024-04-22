# 2024-04-22
d, h, w = map(int, input().split())
y = (d**2 / (1+(h**2/w**2))) ** (1/2)
x = y * h / w
print(f"{int(x)} {int(y)}")