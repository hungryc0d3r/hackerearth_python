testCases = int(input())
ng = []
np = []
for t in range(testCases):
    g = 0
    p = 0

    cost = list(input().split())
    nPart = int(input())
    
    for i in range(nPart):
        
        winList = list(input().split())
        if winList[0] == '1':
            g = g+1
        if winList[1] == '1':
            p = p+1

    ng.append(g)
    np.append(p)
    m = min(((int(ng[t])*int(cost[0])) + (int(np[t])*int(cost[1])), ((int(ng[t])*int(cost[1])) + (int(np[t])*int(cost[0])))))

    print(m)
