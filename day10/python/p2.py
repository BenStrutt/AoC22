lines = open('../input.txt','r').read().split('\n')

image = []
line = []
imageIdx = 0
lineIdx = 0

x = 1
cycle = 1
total = 0

def incrementCycle():
	global cycle, total
	if (cycle + 20) % 40 == 0:
		total += x * cycle
	
	cycle += 1

def drawPixel():
	global image, line, imageIdx, lineIdx
	c = '#' if lineIdx > x - 2 and lineIdx < x + 2 else ' '
	line.append(c)

	lineIdx += 1
	if lineIdx > 39:
		lineIdx = 0
		image.append(line)
		line = []

for l in lines:
	drawPixel()
	incrementCycle()
	if l != 'noop':
		drawPixel()
		incrementCycle()
		amount = l.split(' ')[1]
		x += int(amount)

for imageLine in image:
	for pixel in imageLine:
		print(pixel, end="")
	print("")