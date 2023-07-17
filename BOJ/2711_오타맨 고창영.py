# 소요시간 5분
# map 함수를 자주 쓴다해서 헷갈리지 맙시다...

import sys

test_case_num = int(sys.stdin.readline())
for i in range(test_case_num) :
    typo_index, str = sys.stdin.readline().split()
    typo_index = int(typo_index) - 1
    print(str[0:typo_index] + str[typo_index+1:])