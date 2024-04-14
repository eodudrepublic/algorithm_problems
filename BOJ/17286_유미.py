# 2024-04-14 (04-15)
def get_l(route) :
    l = 0
    for n in range(1, 4) :
        l += ((dic[route[n-1]][0] - dic[route[n]][0])**2 + (dic[route[n-1]][1] - dic[route[n]][1])**2) ** (1/2)
    if l < dic[-1] :
        dic[-1] = l

def fn(n) :
    if n == 3 :
        get_l(route)
        return
    
    for i in range(3) :
        if not visit[i] :
            route[n+1] = i + 1
            visit[i] = True
            fn(n+1)
            visit[i] = False

dic = {-1:1000000}
for _ in range(4) :
    x, y = map(int, input().split())
    dic[_] = (x, y)

route = [0 for _ in range(4)]
visit = [False for _ in range(3)]
fn(0)
print(int(dic[-1]))