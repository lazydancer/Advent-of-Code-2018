def readNode(input):
  result = 0

  childrenCount = input.pop()
  metadataCount = input.pop()

  for _ in range(childrenCount): 
    result += readNode(input)

  for _ in range(metadataCount):
    result += input.pop()

  return result

def rootNode(input):
  

  childrenCount = input.pop()
  metadataCount = input.pop()

  if childrenCount is 0:
    result = 0
    for _ in range(metadataCount):
      result += input.pop()
    return result
  
  else:
    children = []
    result = 0
    
    for _ in range(childrenCount):
      children.append(rootNode(input))

    meta = 0
    for _ in range(metadataCount):
      meta = input.pop()
      if meta <= len(children) and meta > 0:
        result += children[meta-1]

    return result


def main(line):

  input = [int(x) for x in line.split(" ")]
  input = input[::-1] #reverse
  inputCopy = input.copy()

  print('Part 1 :', readNode(input)) #36566
  print('Part 2 :', rootNode(inputCopy)) #30548

inputFile = open('input', 'r')
main(inputFile.readlines()[0])
