import re

def readClaim(claimStr):
  result = claimStr.rstrip() 
  result = claimStr.replace(" ","") 
  result = re.split('@|,|:|x', claimStr[1:])
  
  return list(map(lambda x: int(x), result))

def applyClaim(claim, fabric):
  
  claimId = claim[0]
  claimX = claim[1]
  claimY = claim[2]
  claimWidth = claim[3]
  claimHeight = claim[4]

  for line in fabric[claimY:(claimY+claimHeight)]:
    for element in line[claimX:(claimX+claimWidth)]:
      element.append(claimId)

  return fabric

def countOverlap(fabric):

  count = 0 

  for y in range(1000):
    for x in range(1000):

      if len(fabric[y][x]) > 1:
        count += 1

  return count


def idNotOverlaping(fabric):

  overlaping = set()
  result = 0

  for y in range(1000):
    for x in range(1000):

      if len(fabric[y][x]) > 1:
        for id in fabric[y][x]:
          overlaping.add(id)


  for i in range(1,1384):
    if i not in overlaping:
      result = i

  return result

def generateFabric(claims):

  fabric = [[[] for x in range(1000)] for y in range(1000)] #init fabric
  for claim in claims:
    claimArr = readClaim(claim)
    fabric = applyClaim(claimArr, fabric)

  return fabric

def main():
  inputFile = open('input', 'r')
  lines = inputFile.readlines()

  fabric = generateFabric(lines)

  print("Part 1 - The count of the overlap is", countOverlap(fabric)) # 120408
  print("Part 2 - The only id not overlaping is", idNotOverlaping(fabric)) 

main()