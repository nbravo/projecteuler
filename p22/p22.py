from string import ascii_uppercase as alphUpper

def p22(fileName):
  names = getSortedNames(fileName)

  alphMap = {x:i for i, x in enumerate(alphUpper, 1)}

  currSum = 0
  for i in xrange(0, len(names)):
    currSum += (i+1) * nameScore(names[i], alphMap)
  return currSum

def getSortedNames(fileName):
  with open(fileName) as f:
    content = f.readline()

  names = content.strip('\n').split(',')
  names = [name.strip('"') for name in names]
  names.sort()
  return names

def nameScore(name, alphMap):
  return sum([alphMap[ch] for ch in list(name)])
