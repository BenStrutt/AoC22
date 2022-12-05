def solve(file):
	topCalories = []
	currentCalories = 0

	def compareAndResetCalories():
		nonlocal topCalories
		nonlocal currentCalories

		def replaceLowest(calsList, cals):
			lowestIdx = 0
			lowestNum = calsList[0]
			i = 1
			while i < len(calsList):
				num = calsList[i]
				if calsList[i] < lowestNum:
					lowestNum = num
					lowestIdx = i
				
				i += 1
				
			if cals > lowestNum:
				calsList[lowestIdx] = cals


		if len(topCalories) < 3:
			topCalories.append(currentCalories)
		else:
			replaceLowest(topCalories, currentCalories)

		currentCalories = 0

	def sumIntList(intList):
		sum = 0
		i = 0
		length = len(intList)

		while i < length:
			sum += intList[i]
			i += 1
		
		return sum

	for line in file:
		if line == "\n":
			compareAndResetCalories()
		else:
			currentCalories += int(line.strip())

	file.close()

	compareAndResetCalories()
	print(sumIntList(topCalories))

solve(open("../input.txt"))