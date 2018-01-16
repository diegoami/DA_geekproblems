
from sys import stdin

"""
7 8 2 1 4 3

1. b1, b2 = 8, 7
2. b1, b2 = 8, 7

2 4 5 6 7

1. b1, b2 = 4, 2
2. b1, b2 = 5, 4
3. b1, b2 = 6, 5

2 4 7 5 6

1. b1, b2 = 4 , 2
2. b1, b2 = 7 , 4
3. b1, b2 = 7 , 5
3. b1, b2 = 7 , 6



"""

def scan_once(n, l):
    b1, b2 = -1, -1
    for x in l:
        if x > b1:
            b2, b1 = b1, x
        elif x > b2 and x != b1:
            b2 = x
    return b2





t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    ls =  stdin.readline()
    l = list(map(int ,ls.split()))
    print(scan_once(n ,l))


def second_largest_sorted(n, l):
    sl = sorted(l, reverse=True)
    max_l = sl[0]
    i = 1

    while i < n and sl[i] == max_l:
        i += 1
    if i == n:
        print(-1)
    else:
        print(sl[i])

def find_max_first(n, l):
    max_in_l = max(l)
    i = 0
    ot_max = -1
    for e in l:
        if e < max_in_l and e > ot_max:
            ot_max = e

    return ot_max
