# 2024-01-09
arr = ('baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan')
ru = (2, 3, 6, 7, 10, 11)
n = int(input())
r = (n - 1) // 14
n = (n - 1) % 14
if n not in ru : print(arr[n])
else : 
    ans = arr[n] + 'ru' * r
    if ans.count('r') < 5 : print(ans)
    else : print(f"tu+ru*{ans.count('r')}")