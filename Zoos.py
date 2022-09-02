zin = input()
lz = [i for i in zin]
zcount = lz.count('z')
ocount = lz.count('o')
if zcount == ocount/2:
    print('Yes')
else:
    print('No')
