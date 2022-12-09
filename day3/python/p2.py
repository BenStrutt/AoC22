f = open('../input.txt','r').read().split('\n')
toI = lambda c: ord(c) - (96 if ord(c) > 90 else 38)
lComp = lambda f, i: [c for c in f[i] if c in f[i-1] and c in f[i-2]][0]
sum = 0

for i in range(len(f)):
	if (i%3==2): sum += toI(lComp(f, i))

print(sum)