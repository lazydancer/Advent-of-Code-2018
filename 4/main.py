import re
from datetime import datetime

def readRecords(lines):

  records = []
  for line in lines:
    dateStr = re.match(r"[^[]*\[([^]]*)\]", line).groups()[0]
    date = datetime.strptime(dateStr, "%Y-%m-%d %H:%M" )
    records.append((date, line[19:].rstrip()))
  
  records.sort(key=lambda x: x[0])

  result = []
  id = 0
  for date,text in records:
    awake = None

    searchId = re.search("#[0-9]+", text)
    if searchId:
      id = int(searchId.group()[1:])

    if text == "falls asleep":
      awake = False

    if text == "wakes up":
      awake = True

    result.append((date, id, awake))

  return result

def guardIDs(records):
  guardIDs = set()
  for record in records:
    guardIDs.add(record[1])

  return guardIDs

def guardsRecords(id, records):
  return [x for x in records if x[1] == id]  

def mostAsleepGuard(records):

  minsAsleep = {}
  previoustime = datetime.now()
  for record in records:
    if record[2] is False:
      previoustime = record[0]
    if record[2] is True:
      timeDiff = (record[0] - previoustime).seconds / 60      
      if record[1] not in minsAsleep:
        minsAsleep[record[1]] = 0
      minsAsleep[record[1]] += timeDiff

  return max(minsAsleep.keys(), key=(lambda key: minsAsleep[key]))
  

def minMostAsleep(records):
  sleepyMin = {}
  for i in range(60):
    sleepyMin[i] = 0

  for record in records:
    if record[2] is False:
      previoustime = record[0]
    if record[2] is True:
      timeDiff = int((record[0] - previoustime).seconds / 60)

      for i in range(timeDiff):
        sleepyMin[previoustime.minute + i % 60] += 1


  mostAsleepMin = max(sleepyMin.keys(), key=(lambda key: sleepyMin[key]))
  return (mostAsleepMin, sleepyMin[mostAsleepMin])


def part1(records):
  sleepyGuard = mostAsleepGuard(records)
  sleepyMin, _ = minMostAsleep(guardsRecords(sleepyGuard, records)) 

  print("The solution to part one is ", sleepyGuard, "*", sleepyMin, "=", sleepyGuard * sleepyMin )
  #Guard 2851 on minute 44 = 125444


def part2(records):
  maximum = (0,0,0) #id, min, time

  for guard in guardIDs(records):
    minute, time =  minMostAsleep(guardsRecords(guard, records))
    if time > maximum[2]:
      maximum = (guard, minute, time)

  print("The solution to part two is ", maximum[0], "*", maximum[1], "=", maximum[0] * maximum[1] )
  # Guard 733 at minute 25


def main():

  inputFile = open('input', 'r')
  lines = inputFile.readlines()
  records = readRecords(lines)

  part1(records)
  part2(records)
  
main()

