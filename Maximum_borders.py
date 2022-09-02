t = int(input())
mb = []
for i in range(t):
    rc = input().split()
    row = int(rc[0])
    col = int(rc[1])

    m = 0
    for r in range(row):
        matrix = input()
        bc = 0
        for v in matrix:
            if v=='#':
                bc = bc+1
        if bc >= m:
            m = bc
    mb.append(m)
for val in mb:
    print(val)
