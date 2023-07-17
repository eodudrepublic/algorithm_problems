# 2023-04-18
import sys

string_a = "".join(['-', sys.stdin.readline().strip()])
string_b = "".join(['-', sys.stdin.readline().strip()])
dp = [[0]*(len(string_a)) for _ in range(len(string_b))]

for i in range(1,len(string_b)) :
    for j in range(1,len(string_a)) :
        if string_a[j] == string_b[i] :
            dp[i][j] = dp[i-1][j-1]+1
        else :
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

sys.stdout.write("".join([str(dp[-1][-1]), '\n']))

i, j = len(string_b)-1, len(string_a)-1
ans = '\n'
while i > 0 and j > 0 :
    if dp[i][j] == dp[i][j-1] :
        j-=1
    elif dp[i][j] == dp[i-1][j] :
        i-=1
    else :
        ans = ''.join([string_a[j] + ans])
        i-=1; j-=1
if ans != '\n' :
    sys.stdout.write(ans)