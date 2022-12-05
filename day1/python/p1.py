def solve(file):
	maxCalories = 0
	currentCalories = 0

	def compareAndResetCalories():
		nonlocal maxCalories
		nonlocal currentCalories

		if currentCalories > maxCalories:
			maxCalories = currentCalories

		currentCalories = 0

	for line in file:
		if line == "\n":
			compareAndResetCalories()
		else:
			currentCalories += int(line.strip())

	file.close()

	compareAndResetCalories()
	print(maxCalories)

solve(open("../input.txt"))