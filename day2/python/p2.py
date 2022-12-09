file = open('../input.txt','r').read().split('\n')
mapFunc = lambda str: points[str.replace(' ','')]

opponent = ['A', 'B', 'C']
results = ['X', 'Y', 'Z']
wins = {'A': 'C', 'B': 'A', 'C': 'B'}
losses = {'A': 'B', 'B': 'C', 'C': 'A'}
points = {}

funcs = [
	lambda opp: opponent.index(wins[opp]) + 1,
	lambda opp: 3 + opponent.index(opp) + 1,
	lambda opp: 6 + opponent.index(losses[opp]) + 1
]

score = lambda opp, res: funcs[['X', 'Y', 'Z'].index(res)](opp)

for choice in opponent:
	for outcome in results:
		points[choice + outcome] = score(choice, outcome)

sum = sum(map(mapFunc, file))
print(sum)
