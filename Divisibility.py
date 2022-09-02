N = int(input())
data = [int(x) for x in input().split()]

rem = [int(data[i])%10 for i in range(len(data))]

if rem[-1] == 0:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
