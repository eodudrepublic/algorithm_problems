# 2024-02-01
doc = input()
word = input()

# KMP
doc_len = len(doc)
word_len = len(word)
pi = [0]
for _ in range(1, word_len) :
    temp = pi[-1]
    if word[_] == word[temp] : pi.append(temp + 1)
    else : pi.append(0)

index = 0
temp = 0
ans = 0
while True :
    if index == doc_len : break
    
    if doc[index] == word[temp] : 
        temp += 1
        index += 1
        if temp == word_len :
            ans += 1
            temp = 0
    elif temp != 0 :
        temp = pi[temp-1]
    else :
        index += 1
print(ans)

# # brute force
# dl = len(doc)
# wl = len(word)
# ans = 0
# l = 0
# while True :
#     try :
#         if l == dl : break
#         if doc[l:l+wl] == word : 
#             l += wl
#             ans += 1
#         else : 
#             l += 1
#     except :
#         break
# print(ans)
