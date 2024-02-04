# 2024-02-04 (02-05)
arr = ['U', 'C', 'P', 'C']
sentence = input()
for _ in sentence :
    if _ == arr[0] : 
        arr.pop(0)
        if not arr : break
if not arr : print('I love UCPC')
else : print('I hate UCPC')