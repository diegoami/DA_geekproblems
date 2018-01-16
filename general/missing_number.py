# code
from functools import reduce


def find_missing_number(n, l):
    sl = sorted(l)
    cn = 1
    for el in sl:

        if el != cn:
            return cn
        else:
            cn += 1
    return cn


def find_missing_number_2(n, l):
    er = (n * (n + 1)) / 2
    return int(er - sum(l))


def find_missing_number_3(n, l):
    all_xor = reduce(lambda x, y: x ^ y, range(1, n + 1))
    l_xor = reduce(lambda x, y: x ^ y, l)
    return l_xor ^ all_xor


"""
(1^2^3)^(1^2) = (1^1)^(2^2)^3 = 0^0^3 = 3 


1+2+3+4+...+n = n*(n+1)/2
n: 10 = 45

1+2+3+4+5 = 15 


"""

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    mn = find_missing_number_3(n, l)
    if mn:
        print(mn)
    else:
        print(-1)