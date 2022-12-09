f = open('../input.txt','r').read().split('\n')
toI = lambda c: ord(c) - (96 if ord(c) > 90 else 38)
lComp = lambda i: [c for c in f[i] if c in f[i+1] and c in f[i+2]][0]

print(sum(map(lambda i: toI(lComp(i)), range(len(f))[::3])))