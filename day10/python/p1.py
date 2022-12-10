lines = open('../input.txt','r').read().split('\n')
x = 1
cycle = 1
total = 0

def incrementCycle():
	global cycle, total
	if (cycle + 20) % 40 == 0:
		total += x * cycle
	
	cycle += 1

for line in lines:
	incrementCycle()
	if line != 'noop':
		incrementCycle()
		amount = line.split(' ')[1]
		x += int(amount)

print(total)