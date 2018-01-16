# code

"""
1 2 3 7 5

s1:1  : 1
s1:2, s2:2 : 3, 2
s1:3, s2:3, s3:3 : 6, 4, 3



1 2 3 7 5
b = 0, s: 1 < 12 , a = 0
b = 1, s: 3 < 12 , a = 0
b = 2, s: 6 < 12 , a = 0
b = 3, s: 6+7 > 12, a = 0
b = 3, s: 12 = 12, a = 1


"""
from sys import stdin


def find_indexes_better(n, se, l):
    s = 0
    a, b = 0, 0
    for b in range(n):
        while s + l[b] > se:
            s -= l[a]
            a += 1

        if s + l[b] < se:
            s += l[b]
        elif s + l[b] == se:
            return a + 1, b + 1
    return None, None


def find_indexes(n, se, l):
    s = {}
    for i, e in enumerate(l):
        for j in range(0, i + 1, 1):
            s[j] = s.get(j, 0) + e
            if s[j] == se:
                return j + 1, i + 1
    return None, None


t = int(stdin.readline())
for _ in range(t):
    n, se = map(int, stdin.readline().split())
    l = list(map(int, stdin.readline().split()))
    a, b = find_indexes_better(n, se, l)
    if a and b:
        print(a, b)
    else:
        print(-1)

