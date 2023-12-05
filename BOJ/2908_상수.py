# 2023-12-05 (12-06)
a, b = input().split()
ra = rb = ''
for _ in reversed(a) : ra += _
for _ in reversed(b) : rb += _
print(max(ra, rb))