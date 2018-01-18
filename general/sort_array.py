# codet = int(input())

def sort_list_012(n, l):
    return sorted(l)


"""
0 2 1 2 0

lo, mi, hi

lo,mi,hi = 0,0,4
1: 
    mie == 0, lo++, mi++
    lo,mi,hi = 1,1,4
2: 
    mie == 2
    0 0 1 2 2
    hi-- , mi++
    lo,mi,hi = 1,2,3
3:  
    mie == 1
    0 0 1 2 2
    mi +++
    lo, mi, hi = 1, 3, 3
4:
    mie == 2
    0 0 1 2 2
    mi ++
    lo, mi, hi =1, 4, 3


0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1
lo, mi, hi = 0, 0, 11
mi:
1:  
    lo, mi, hi = 1, 1, 12
    0 1 1 0 1 2 1 2 0 0 0 1
    lo, mi, hi = 2, 2, 12

2:
    lo, mi, hi = 2, 2, 12
    lo, mi, hi = 2, 3, 12
3:
    lo, mi, hi = 2, 3, 12
    lo, mi, hi = 2, 4, 12
4:
    lo, mi, hi = 2, 4, 12
    0 0 1 1 1 2 1 2 0 0 0 1
    lo, mi, hi = 3, 5, 12
5:
    lo, mi, hi = 3, 5, 12
    0 0 1 1 1 2 1 2 0 0 0 1
    lo, mi, hi = 3, 6, 12
6:
    lo, mi, hi = 3, 6, 12
    0 0 1 1 1 1 1 2 0 0 0 2
    lo, mi, hi = 3, 7, 11
7:
    lo, mi, hi = 3, 7, 11
    0 0 1 1 1 1 1 2 0 0 0 2
    lo, mi, hi = 3, 8, 11
8a:
    lo, mi, hi = 3, 8, 11
    0 0 1 1 1 1 1 0 0 0 2 2
    lo, mi, hi = 3, 8, 10
8b:  
    lo, mi, hi = 3, 8, 10
    0 0 0 1 1 1 1 1 0 0 2 2
    lo, mi, hi = 4, 9, 10
9:
    lo, mi, hi = 4, 9, 10
    0 0 0 0 1 1 1 1 1 0 2 2
    lo, mi, hi = 5, 10, 10
10:
    lo, mi, hi = 5, 10, 10
    0 0 0 0 0 1 1 1 1 1 2 2
    lo, mi, hi = 5, 11, 10
"""


def sort_list_2(n, l):
    lo, mi, hi = 0, 0, n - 1
    while mi <= hi:
        #        print("B: {}, {}, {}".format(lo+1,mi+1,hi+1))
        #        print("B: {}".format(l))

        if l[mi] == 0:
            l[mi], l[lo] = l[lo], l[mi]
            lo += 1
            mi += 1
        elif l[mi] == 2:
            l[mi], l[hi] = l[hi], l[mi]
            hi -= 1
        elif l[mi] == 1:
            mi += 1

    #        print("A: {}, {}, {}".format(lo+1,mi+1,hi+1))
    #        print("A: {}".format(l))

    return l


from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    sl = sort_list_2(n, l)
    print(*sl, sep=' ')