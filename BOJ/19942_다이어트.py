# 2023-05-29 (05-30)
import sys
from itertools import combinations

total_p = total_f = total_c = total_v = 0
I = int(sys.stdin.readline())
sp, sf, sc, sv = map(int, sys.stdin.readline().split())

ingredients = [()]
for i in range(I) :
    p, f, c, v, price = map(int, sys.stdin.readline().split())
    ingredients.append((p, f, c, v, price))

INF = 1e9

min_price = INF
answer = None
for cnt in range(1, I+1) :
    for comb in combinations(range(1, I+1), cnt) :
        tp = tf = tc = tv = tprice = 0
        for target in comb :
            tp += ingredients[target][0]
            tf += ingredients[target][1]
            tc += ingredients[target][2]
            tv += ingredients[target][3]
            tprice += ingredients[target][4]
        
        if tp < sp or tf < sf or tc < sc or tv < sv or tprice > min_price :
            continue
        
        if tp >= sp and tf >= sf and tc >= sc and tv >= sv :
            if min_price > tprice :
                min_price = tprice
                answer = comb
            elif min_price == tprice :
                answer = sorted([answer, comb])[0]

if min_price == INF : sys.stdout.write('-1\n')
else : 
    sys.stdout.write(''.join([str(min_price), '\n']))
    for _ in answer :
        sys.stdout.write(''.join([str(_), ' ']))
    sys.stdout.write('\n')