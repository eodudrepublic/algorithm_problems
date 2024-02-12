# 2024-02-12 (02-13)
yes = ('3', '6', '9')
no = ('0', '1', '2', '4', '5', '7', '8')

def func(x) :
    if x in no : return 'NO'
    if x in yes : return 'YES'
    
    y = 0
    for _ in x :
        y += int(_)
    return str(y)

n = input()

ans = 0
while True :
    temp = func(n)
    if temp == 'YES' or temp == 'NO' : 
        print(ans)
        print(temp)
        break
    else :
        ans += 1
        n = temp