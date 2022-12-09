f = open('../input.txt','r').read().split('\n')
l = lambda s: len(s)//2
toI = lambda c: ord(c) - (96 if ord(c) > 90 else 38)
mapFunc = lambda s: toI([x for x in s[:l(s)] if x in s[l(s):]][0])

print(sum(map(mapFunc, f)))