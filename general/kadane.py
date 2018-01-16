"""
-1 3 -2 6

x : -1 , s[0] : -1
x : 3 , s[0] : 2, s[1] : 3
x : -2,  s[0] :  0, s[1] : 1, s[2] : -2
x : 6,  s[0] : 6, s[1] : 7, s[2] : 4, s[3] : 6


"""
"""
-1 3 -2 6

x : -1 , s[0] : -1
x : 3 , s[0] : 2, s[1] : 3
x : -2,  s[0] :  0, s[1] : 1, s[2] : -2
x : 6,  s[0] : 6, s[1] : 7, s[2] : 4, s[3] : 6


"""

inputarray =[
"4",
"3",
"1 2 3",
"4",
"-1 -2 -3 -4",
"4",
"-1 3 -2 6",
"8",
"-2 -3 4 -1 -2 1 5 -3"
]
"""
max_so_far --> sf
max_ending_here --> eh

case : -1 -2 -3 -4
1 : sf = -1, eh = max(-1,0) = 0
2 : sf = -1, eh = max(-2,0) = 0
... sf = -1

case: -1 3 -2 6
1: sf = -1, eh = max(-1,0) = 0
2: sf = 3, eh = 0+3= 3  
3: sf = 3, eh = 3+-2 >0 = 1
4: sf = 7, eh = 1+6 = 7

case: -2 -3 4 -1 -2 1 5 -3

1: sf: -2, eh = 0
2: sf: -2, eh = 0
3: sf: 4,  eh = 0+4
4: sf: 4 ,  eh= 4-1 =3
5: sf: 4 ,  eh= 3-2 =1
6: sf: 4 , eh = 1+1 = 2
7: sf: 7 , eh =2+5 =7
"""
from tools import input, initArrayInputter
initArrayInputter(inputarray)

def find_best_sum_2(n, l):
    sf, eh = l[0], max(l[0],0)
    for x in l[1:]:
        eh = max(eh+x,0)
        if eh > sf:
            sf = eh
    return sf



def find_best_sum(n, l):
    s = {}
    cm = l[0]
    for i, e in enumerate(l):
        for j in range(0, i + 1):
            s[j] = s.get(j, 0) + e
            if s[j] > cm:
                cm = s[j]

    return cm


t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    cm = find_best_sum_2(n, l)
    if cm:
        print(cm)
    else:
        print(-1)