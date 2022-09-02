n = int(input())

fa = list(map(int, input().split()))
sa = list(map(int, input().split()))

mv = min(fa)
c = 0
i=0
while i < n:
    while fa[i]>mv:
        fa[i] = fa[i] - sa[i]
        c = c+1
    if fa[i]<mv:
        mv = fa[i]
        i = 0
    elif fa[i] < 0:
        c = -1
        break
    else: i = i+1

print(c)
