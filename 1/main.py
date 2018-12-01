def loadInput(file):
	inputFile = open(file, 'r')
	inputArray = []

	for line in inputFile.readlines():
		if line[0] is '+':
			inputArray.append(int(line[1:]))
		elif line[0] is '-':
			inputArray.append(-1 * int(line[1:]))
		else:
			raise ValueError('Value missed + and - values', line)

	return inputArray

def main():
	
	changeOfFrequencies = loadInput('day1_input')

	print('Part 1 result is: ', sum(changeOfFrequencies)) # 493

	acc = 0
	seen = {acc}
	part2result = 0

	while part2result is 0:
		for change in changeOfFrequencies:
			acc += change
			if acc in seen:
				part2result = acc
				break
			seen.add(acc)

	print('Part 2 result is: ', part2result) # 413
main()