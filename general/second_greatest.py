from sys import stdin

inputarray =[
"2",
"5",
"2 4 5 6 7",
"6",
"7 8 2 1 4 3"
]


def input():
    return stdin.readeline()


from tools import input, initArrayInputter
initArrayInputter(inputarray)


t = int(input())
for _ in range(t):
    n = int(input())
    ls = input()
    l = map(int, ls.split())
    sl = sorted(l, reverse=True)
    max_l = sl[0]
    i = 1

    while i < n and sl[i] == max_l:
        i += 1
    if i == n:
        print(-1)
    else:
        print(sl[i]) 
