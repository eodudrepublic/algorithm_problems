# 2023-12-20 (12-21)
odd = (0, 2, 4, 6)
even = (1, 3, 5, 7)

count = 0
for i in range(8) :
    line = input()
    if i % 2 == 0 :
        for _ in odd : 
            if line[_] == 'F' : count += 1
    else :
        for _ in even : 
            if line[_] == 'F' : count += 1
print(count)