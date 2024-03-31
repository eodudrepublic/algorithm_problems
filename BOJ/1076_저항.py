# 2024-03-30
arr1 = {
    'black':'0',
    'brown':'1',
    'red':'2',
    'orange':'3',
    'yellow':'4',
    'green':'5',
    'blue':'6',
    'violet':'7',
    'grey':'8',
    'white':'9'
}

arr2 = {
    'black':1,
    'brown':10,
    'red':100,
    'orange':1000,
    'yellow':10000,
    'green':100000,
    'blue':1000000,
    'violet':10000000,
    'grey':100000000,
    'white':1000000000

}

temp = ''
for _ in range(2) :
    i = input()
    temp += arr1[i]
ans = int(temp)
i = input()
ans *= arr2[i]
print(ans)