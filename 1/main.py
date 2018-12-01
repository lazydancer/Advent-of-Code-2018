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

	seenFrequencies = set()
	i = 0
	frequency = 0

	while frequency not in seenFrequencies:
		
		seenFrequencies.add(frequency)

		frequency += changeOfFrequencies[i]

		if i < len(changeOfFrequencies)-1:
			i += 1
		else: 
			i = 0


	print('Part 2 result is: ', frequency) # 413
main()