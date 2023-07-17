import sys
from collections import defaultdict


def is_possible(s, t):
    if len(s) < len(t):
        return False
    elif len(s) == len(t):
        return s == t
    else:
        return calc(s, t)


def calc(s, t):
    length = len(s)
    t_length = len(t)
    if t_length == 1 :
        for i in s :
            if i == t :
                return True
    words = defaultdict(set)
    words[length].add(s)

    while length > t_length:
        for word in words[length]:
            for i in range(len(word)):
                if i == 0:
                    new_word = word[1:]
                elif i <= len(word)-2:
                    new_word = word[:i-1] + word[i+1:]
                else:
                    new_word = word[:i-1]

                if len(new_word) >= t_length:
                    words[len(new_word)].add(new_word)

        length -= 1

    if t in words[t_length]:
        return True
    else:
        return False


n_ = int(input())

for _ in range(n_):
    s_ = sys.stdin.readline().rstrip()
    t_ = sys.stdin.readline().rstrip()

    if is_possible(s_, t_):
        print("YES")
    else:
        print("NO")