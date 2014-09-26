from string import ascii_uppercase as alphUpper

def p42(fileName):
  words = fileToWords(fileName)

  # Set up triangle numbers
  maxLen = len(max(words, key=len))
  maxTriNum = maxLen * 26

  triNums = generateTriNums(maxTriNum)

  alphDict = {x:i for i, x in enumerate(alphUpper, 1)}

  numTriWords = 0
  for word in words:
    if score(word, alphDict) in triNums:
      numTriWords += 1

  return numTriWords

def fileToWords(fileName):
  with open(fileName) as f:
    content = f.readlines()[0]

  words = []
  for word in content.split(','):
    words.append(word.strip('"'))
  return words

def generateTriNums(maxTriNum):
  triNums = []
  n = 2
  nextTriNum = 1
  while (nextTriNum <= maxTriNum):
    triNums.append(nextTriNum)
    nextTriNum = (n * (n+1))/2
    n += 1
  return triNums

def score(word, alphDict):
  return sum([alphDict[ch] for ch in list(word)])
